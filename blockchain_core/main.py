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

from Wallet.wallet import Wallet
from Wallet.transaction import Transaction
from Core import Core

HASH = '0000000000000000000000000000000000000000000000000000000000000000'
NONE = '----------------------------------------------------------------'
user1_id = 'f71f0c070d1ece7c135da3d8843df403c781fa4bf83ea9f3f0995108ee52d532'
user2_id = '89b98fc3e796e750ebce49c63b69e6fa4e6c3f096b9b93bfba5bcc48ab0c9ad5'
token = ['df3e6b0bb66ceaadca4f84cbc371fd66e04d20fe51fc414da8d1b84d31d178de',
         'd8cc7aed3851ac3338fcc15df3b6807b89125837f77a75b9ecb13ed2afe3b49f',
         '5d6b091416885eaa91283321b69dc526fc42c97783e4cdfdff7a945e3be1f9ef',
         '4cb0ea499ca7177d32b4deb6e251d0a8f857f91d078af209b7d354528ef62201',
         'aa1f6f7084d4030e09f5542aa22e7947a81cec2966a251da748cfb501ace6ddc',
         '8675c9c1f6558212f7f95f5308c03655067e925157ed6e65f024aefadfc7d64f']

def main():
    now = datetime.datetime.now()
           
    blockChain = Blockchain(BlockchainInit.SOURCE)
    #state, my_item = Pool.construct(user1_id, poolParam.SEND.value, user2_id, 50.0, str(now), HASH)
    #state, my_item = Pool.construct(token[1], poolParam.nTOKEN.value, user1_id, 1, str(now), HASH)
    #blockChain.add_pool(my_item)
    
    core = Core()
    core.contruct_wallets_from_blockchain(blockChain)
    
    
    
    #state, bb = blockChain.get_block(1)
    
    #st, pp = Block.get_pool(1, bb)
    #st2, str_ = Pool.print_pool(pp)
    #print(str_)
    
    ###############
    #state, wallet = Wallet.construct(user1_id)
    #state = Wallet.save_wallet(wallet, 1)
    #state, pool = Pool.construct(user2_id, poolParam.nUSER.value, NONE, 1, str(now), HASH)
    #state = blockChain.add_pool(pool)
    ###############
    
    #transaction = Transaction.construct(user1_id, user2_id, 50.0, 'IN', str(now))
    #Wallet.add_transaction(wallet, transaction)

    st = blockChain.print_blocks() # blockChain.print_blocks([2])
    print (st)
    
    #state, wallet = Wallet.read_wallet(2)
    #print(state)
    
    #st, wallet = Wallet.add_amount(wallet, 100.0)
    #print(wallet.bilance)
    #st, wallet = Wallet.remove_amount(wallet, 99.0)
    #print(wallet.bilance)
    
    #sdsd, wallet = Wallet.add_transaction(wallet, user1_id, user2_id, 50.0)
    #print(wallet.transactions)
    #print(wallet.bilance)
    
if __name__ == "__main__":
    main()

