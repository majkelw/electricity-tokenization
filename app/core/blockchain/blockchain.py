import hashlib
from enum import Enum
from core.blockchain.pool import poolParam

from core.blockchain.block import Block


class Blockchain:
    BlockchainStats = Enum('BlockchainStats', ['STATE_OK', 'BLOCK_NOT_EXIST'])
    DIR_TO_BLOCKS = "core/data/blocks/"
    blocks = []

    def __init__(self):
        # try to read blocks
        while True:
            state, block = Block.read_block(len(self.blocks))  # start from index 0
            if state == Block.BlockStats.STATE_OK:
                self.blocks.append(block)
            else:
                break

        # if no blocks detected create one
        if len(self.blocks) == 0:
            state, block = Block.construct()
            self.blocks.append(block)
            Block.save_block(self.blocks[len(self.blocks) - 1], len(self.blocks) - 1)

    def add_pool(self, pool):
        state, num_pool = Block.add_pool(self.blocks[-1], pool)

        if state == Block.BlockStats.BLOCK_FULL:
            Block.save_block(self.blocks[-1], len(self.blocks) - 1)
            self.blocks.append(Block(self.blocks[-1].endHash, self.calculate_new_HASH(), [pool]))

        Block.save_block(self.blocks[-1], len(self.blocks) - 1)

        return self.BlockchainStats.STATE_OK

    def calculate_new_HASH(self):
        str_ = ""
        for pool in self.blocks[-1].pools:
            sub_str_ = "".join([pool.id_1, pool.id_2, pool.id_3, pool.time])
            str_ += sub_str_

        return hashlib.sha256(str_.encode('utf-8')).hexdigest()

    def print_blocks(self, list_=None):
        str_ = ""

        if list_ is None:
            for i in self.blocks:
                state, strr = Block.print_block(i)
                str_ += strr
        else:
            for i in list_:
                state, strr = Block.print_block(self.blocks[i])
                str_ += strr

        return str_

    def get_block(self, block_id):
        if block_id <= len(self.blocks) - 1:
            return self.BlockchainStats.STATE_OK, self.blocks[block_id]
        else:
            return self.BlockchainStats.BLOCK_NOT_EXIST, None

    def is_token_deleted(self, token):
        for block in self.blocks:
            for pool in block.pools:
                if pool.param == poolParam.dTOKEN.value and pool.id_1 == token:
                    return True
        return False

    def find_first_not_deleted_user_token(self, user_id):
        for block in self.blocks:
            for pool in block.pools:
                if pool.param == poolParam.nTOKEN.value and pool.id_2 == user_id:
                    if not self.is_token_deleted(pool.id_1):
                        return pool.id_1
        return None

    def to_json(self):
        blocks = []
        block_number = 0

        for block in self.blocks:
            pools = []
            for pool in block.pools:
                pools.append({"id_1": pool.id_1, "id_2": pool.id_2,
                              "id_3": pool.id_3, "param": pool.param, "amount": pool.amount})
            blocks.append({"begin_hash": block.beginHash, "pools": pools,
                           "end_hash": block.endHash})
            block_number += 1
        return {"blocks": blocks}
