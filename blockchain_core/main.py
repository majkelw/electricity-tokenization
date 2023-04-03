import datetime
import pickle
from enum import Enum
from prettytable import PrettyTable
import hashlib

from Blockchain.pool import Pool
from Blockchain.pool import poolParam
from Blockchain.block import Block
from Blockchain.blockchain import Blockchain
from Blockchain.blockchain import BlockchainInit

HASH = '0000000000000000000000000000000000000000000000000000000000000000'

def main():
    now = datetime.datetime.now()
    
    state, my_item = Pool.construct(HASH, poolParam.SEND.value, HASH, 1, str(now), HASH)
       
    blockChain = Blockchain(BlockchainInit.SOURCE)
    blockChain.add_pool(my_item)
    blockChain.print_blocks()
    
    

if __name__ == "__main__":
    main()

