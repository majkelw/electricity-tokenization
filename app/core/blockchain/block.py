from typing import NamedTuple
from enum import Enum
import pickle
import datetime
from prettytable import PrettyTable

from app.core.blockchain.pool import Pool


class Block(NamedTuple):
    beginHash: str
    endHash: str
    pools: list

    DIR_TO_BLOCKS = "core/data/blocks/"
    FILE_NAME_PREF = "BLOCK"

    BlockStats = Enum('BlockStats',
                      ['STATE_OK', 'UNABLE_TO_OPEN', 'NOT_FOUND', 'UNABLE_TO_SAVE', 'ADD_POOL', 'BLOCK_FULL',
                       'POOL_NOT_EXIST'])
    HASH_TEMPLATE = '0000000000000000000000000000000000000000000000000000000000000000'
    NUMBER_OF_POOLS = 2

    pool_idx = 0

    @classmethod
    def construct(self):
        now = datetime.datetime.now()
        state, empty_pool = Pool.construct(self.HASH_TEMPLATE, poolParam.NOTHING.value, self.HASH_TEMPLATE, 0, str(now),
                                           self.HASH_TEMPLATE)
        block = Block(self.HASH_TEMPLATE, self.HASH_TEMPLATE, [empty_pool])
        return (self.BlockStats.STATE_OK, block)

    @classmethod
    def save_block(self, block, blockID):
        block_name = self.DIR_TO_BLOCKS + self.FILE_NAME_PREF + str(blockID) + '.pkl'
        try:
            with open(block_name, 'wb') as f:
                pickle.dump(block, f)
                f.close()
            return (self.BlockStats.STATE_OK)
        except IOError:
            return (self.BlockStats.UNABLE_TO_SAVE)

    @classmethod
    def read_block(self, blockID):
        block_name = self.DIR_TO_BLOCKS + self.FILE_NAME_PREF + str(blockID) + '.pkl'
        try:
            with open(block_name, 'rb') as f:
                block = pickle.load(f)
                f.close()
            return (self.BlockStats.STATE_OK, block)
        except FileNotFoundError:
            return (self.BlockStats.NOT_FOUND, None)
        except IOError:
            return (self.BlockStats.UNABLE_TO_OPEN, None)

    @classmethod
    def add_pool(self, block, pool):
        self.pool_idx = len(block.pools)

        if self.pool_idx < self.NUMBER_OF_POOLS:
            block.pools.append(pool)
            return (self.BlockStats.ADD_POOL, self.pool_idx)
        else:
            return (self.BlockStats.BLOCK_FULL, self.pool_idx)

    @classmethod
    def print_block(self, block):
        str_ = "Begin HASH: " + block.beginHash + "\n"

        x = PrettyTable()
        x.field_names = ["ID1", "PARAM", "ID2", "AMOUNT", "TIME", "ID3"]
        for pool in block.pools:
            state, pool_st = Pool.print_pool(pool)
            x.add_row(pool_st)
        str_ += str(x)

        str_ += "\nEnd HASH: " + block.endHash + "\n\n"
        return (self.BlockStats.STATE_OK, str_)

    @classmethod
    def get_pool(self, pool_id, block):
        if pool_id <= len(block.pools) - 1:
            return (self.BlockStats.STATE_OK, block.pools[pool_id])
        else:
            return (self.BlockStats.POOL_NOT_EXIST, None)
