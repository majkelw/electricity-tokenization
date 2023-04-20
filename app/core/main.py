import datetime
import pickle
from enum import Enum
from prettytable import PrettyTable
import hashlib

from blockchain.pool import Pool
from blockchain.pool import poolParam
from blockchain.block import Block
from blockchain.blockchain import Blockchain

from wallet.wallet import Wallet
from wallet.transaction import Transaction
from core import Core

import random
import hashlib

HASH = '0000000000000000000000000000000000000000000000000000000000000000'
NONE = '----------------------------------------------------------------'
user1_id = 'f71f0c070d1ece7c135da3d8843df403c781fa4bf83ea9f3f0995108ee52d532'
user2_id = '89b98fc3e796e750ebce49c63b69e6fa4e6c3f096b9b93bfba5bcc48ab0c9ad5'

def calculate_new_HASH():
    random_bits = random.getrandbits(128)
    str_ = str(random_bits)
    return hashlib.sha256(str_.encode('utf-8')).hexdigest()

def main():
    now = datetime.datetime.now()

    blockChain = Blockchain()
    core = Core()
    core.contruct_wallets(blockChain)

    # core.add_user(user2_id, blockChain)
    #core.add_user(user1_id, blockChain)

    #for i in range(0, 50):
    #    hash1 = calculate_new_HASH()
    #    core.add_token(hash1, user1_id, blockChain)

    #core.add_transaction(user1_id, user2_id, 50, blockChain)
    #core.add_transaction(user1_id, user2_id, 1, blockChain)
    #core.add_transaction(user1_id, user2_id, 19, blockChain)
    #core.add_transaction(user1_id, user2_id, 25, blockChain)


    st = blockChain.print_blocks() # blockChain.print_blocks([2])
    #print (st)

    core.print_wallet(core.wallets[0])
    # core.print_wallet(core.wallets[1])

if __name__ == "__main__":
    main()

