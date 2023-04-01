import datetime
import pickle
from enum import Enum
from prettytable import PrettyTable
import hashlib

from parameters import *
from blockchain_struct import *

HASH = '0000000000000000000000000000000000000000000000000000000000000000'

class BlockChainCore():
    def __init__(self, num_of_pools_, dir_to_blocks_, state):
        self.num_of_pools = num_of_pools_
        self.dir_to_blocks = dir_to_blocks_
        self.currentBlock = 0
        self.currentPool = 0

        if state == InitializeOpt.BASED:
            now = datetime.datetime.now()
            empty_pool = Pool(HASH, poolParam.NOTHING, HASH, 0, str(now), HASH)
            self.blockChain = BlockChain([Block(HASH,
                                                HASH,
                                                [empty_pool for i in range(0, self.num_of_pools + 1)])])
            
            
                                                
            self.save_block(self.currentBlock)

        elif state == InitializeOpt.SOURCE:
            block = self.read_block(self.currentBlock)
            self.blockChain = BlockChain([block])

            self.currentBlock = len(self.blockChain.blocks)
            self.currentPool = len(self.blockChain.blocks[-1].pools)

            while True:
                block = self.read_block(self.currentBlock)
                
                if block != Errors.END_OF_BLOCKS:
                    self.blockChain.blocks.append(block)
                    self.currentBlock = len(self.blockChain.blocks)
                    self.currentPool = len(self.blockChain.blocks[-1].pools)
                else:
                    self.currentBlock = len(self.blockChain.blocks) - 1
                    self.currentPool = len(self.blockChain.blocks[-1].pools) - 1
                    break
        else:
            print()
         
    def add_pool(self, Pool_):
        if (poolParam.has_value(Pool_.param)
            and len(Pool_.id_1) == len(HASH)
            and len(Pool_.id_2) == len(HASH)
            and len(Pool_.id_3) == len(HASH)):
            if self.currentPool >= self.num_of_pools:
                self.save_block(self.currentBlock)
                self.blockChain.blocks.append(Block(self.blockChain.blocks[-1].endHash,
                                                    self.calculate_new_HASH(),
                                                    [Pool_]))
                self.currentPool = 0
            else:
                self.blockChain.blocks[self.currentBlock].pools.append(Pool_)
                self.currentPool = len(self.blockChain.blocks[-1].pools) - 1

            self.currentBlock = len(self.blockChain.blocks) - 1         
            self.save_block(self.currentBlock)
            
            return Errors.STATE_OK
        
        elif not poolParam.has_value(Pool_.param):
            return Errors.INCONSISTENT_POOL_PARAM
        
        else:
            return Errors.INCONSISTENT_HASH_LEN
        
    def save_block(self, blockID):
        block_name = 'BLOCK' + str(blockID) + '.pkl'
        with open(self.dir_to_blocks + block_name, 'wb') as f:
            pickle.dump(self.blockChain.blocks[blockID], f)
            f.close()

    def read_block(self, blockID):
        block_name = 'BLOCK' + str(blockID) + '.pkl'
        try:
            with open(self.dir_to_blocks + block_name, 'rb') as f:
                block = pickle.load(f)
                f.close()
            return block
        except Exception:
            return Errors.END_OF_BLOCKS
            
    def calculate_new_HASH(self):
        str_ = ""
        for pool in self.blockChain.blocks[-1].pools:
            sub_str_ = "".join([pool.id_1, pool.id_2, pool.id_3, pool.time]) 
            str_ += sub_str_
        
        return hashlib.sha256(str_.encode('utf-8')).hexdigest()

    def print_block(self, blockID):
        print("Begin HASH: " + self.blockChain.blocks[blockID].beginHash)
        
        x = PrettyTable()
        x.field_names = ["ID1", "PARAM", "ID2", "AMOUNT", "TIME", "ID3"]
        for pool in self.blockChain.blocks[blockID].pools:
            x.add_row([pool.id_1[:3] + '...' + pool.id_1[-3:],
                       pool.param,
                       pool.id_2[:3] + '...' + pool.id_2[-3:],
                       str(pool.amount),
                       pool.time,
                       pool.id_3[:3] + '...' + pool.id_3[-3:]])
        
        print(x)
        print("End HASH: " + self.blockChain.blocks[blockID].endHash)
        print()

    def print_blocks(self):
        for i in range(0, len(self.blockChain.blocks)):
            self.print_block(i)

def main():
    now = datetime.datetime.now()
    
    my_item = Pool(HASH, poolParam.SEND.value, HASH, 1, str(now), HASH)
    my_item2 = Pool(HASH, poolParam.SEND.value, HASH, 1, str(now), HASH)
        
    blockChainCore = BlockChainCore(2, "", InitializeOpt.SOURCE)
    #blockChainCore.add_pool(my_item)
    
    blockChainCore.print_blocks()

if __name__ == "__main__":
    main()

