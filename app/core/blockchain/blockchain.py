import hashlib
from enum import Enum

from app.core.blockchain.block import Block


class BlockchainInit(Enum):
    BASED = 0
    SOURCE = 1


class Blockchain():
    blocks = []

    BlockchainStats = Enum('BlockchainStats', ['STATE_OK', 'BLOCK_NOT_EXIST'])

    def __init__(self, state):
        self.currentBlock = 0

        if state == BlockchainInit.BASED:
            state, block = Block.construct()
            self.blocks.append(block)
            Block.save_block(self.blocks[self.currentBlock], self.currentBlock)

        elif state == BlockchainInit.SOURCE:
            blockStat, block = Block.read_block(self.currentBlock)
            self.currentBlock += 1

            if blockStat == Block.BlockStats.STATE_OK:
                self.blocks.append(block)

            while True:
                blockStat, block = Block.read_block(self.currentBlock)
                if blockStat == Block.BlockStats.STATE_OK:
                    self.blocks.append(block)
                    self.currentBlock += 1
                else:
                    break

    def add_pool(self, Pool_):
        state, num_pool = Block.add_pool(self.blocks[-1], Pool_)

        if (state == Block.BlockStats.BLOCK_FULL):
            Block.save_block(self.blocks[-1], len(self.blocks) - 1)
            self.blocks.append(Block(self.blocks[-1].endHash, self.calculate_new_HASH(), [Pool_]))

        Block.save_block(self.blocks[-1], len(self.blocks) - 1)

        return (self.BlockchainStats.STATE_OK)

    def calculate_new_HASH(self):
        str_ = ""
        for pool in self.blocks[-1].pools:
            sub_str_ = "".join([pool.id_1, pool.id_2, pool.id_3, pool.time])
            str_ += sub_str_

        return hashlib.sha256(str_.encode('utf-8')).hexdigest()

    def print_blocks(self, list_=None):
        str_ = ""

        if list_ == None:
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
            return (self.BlockchainStats.STATE_OK, self.blocks[block_id])
        else:
            return (self.BlockchainStats.BLOCK_NOT_EXIST, None)
