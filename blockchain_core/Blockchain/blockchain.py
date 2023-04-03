from typing import NamedTuple
import pickle
from prettytable import PrettyTable
import hashlib
import datetime
from Blockchain.pool import Pool
from Blockchain.pool import poolParam
from Blockchain.block import Block
from enum import Enum

class BlockchainInit(Enum):
    BASED = 0
    SOURCE = 1

class Blockchain():
    blocks = []
    
    def __init__(self, state):
        self.currentBlock = 0

        if state == BlockchainInit.BASED:
            state, block =  Block.construct()
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
            
    def calculate_new_HASH(self):
        str_ = ""
        for pool in self.blocks[-1].pools:
            sub_str_ = "".join([pool.id_1, pool.id_2, pool.id_3, pool.time]) 
            str_ += sub_str_
        
        return hashlib.sha256(str_.encode('utf-8')).hexdigest()

    def print_blocks(self):
        for i in self.blocks:
            ss, stt = Block.print_block(i)
            print(stt)

