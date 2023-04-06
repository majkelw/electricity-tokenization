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
from Wallet.operation import Operation

class Core():
    users_id = []
    wallets = []
    tokens = []

    def contruct_wallets_from_blockchain(self, blockChain):
        walletIdx = 0
        now = datetime.datetime.now()

        for block in blockChain.blocks:
            for pool in block.pools:

                if pool.param == 3:
                    state, wallet = Wallet.construct(pool.id_1)
                    #################################################
                    Wallet.add_amount(wallet, 250)
                    #################################################
                    
                    self.wallets.append(wallet)
                    self.users_id.append(pool.id_1)
                    walletIdx += 1
                    
                elif pool.param == 0:
                    state, transaction1 = Transaction.construct(pool.id_1, pool.id_2, pool.amount, 'OUT', str(now))
                    state, transaction2 = Transaction.construct(pool.id_1, pool.id_2, pool.amount, 'IN', str(now))
                    
                    index1 = [index for index in range(len(self.users_id)) if self.users_id[index] == pool.id_1]
                    index2 = [index for index in range(len(self.users_id)) if self.users_id[index] == pool.id_2]
                    
                    Wallet.add_transaction(self.wallets[index1[0]], transaction1)
                    Wallet.add_transaction(self.wallets[index2[0]], transaction2)

                    Wallet.remove_amount(self.wallets[index1[0]], pool.amount)
                    Wallet.add_amount(self.wallets[index2[0]], pool.amount)

                elif pool.param == 1:
                    index2 = [index for index in range(len(self.users_id)) if self.users_id[index] == pool.id_2]
                    state, operation = Operation.construct(pool.id_2, 1, 'NEW TOKEN', str(now))
                    Wallet.add_operation(self.wallets[index2[0]], operation)
                    Wallet.add_amount(self.wallets[index2[0]], 1)
                    self.tokens.append(pool.id_1)
        
        st, st_ = Wallet.print_status(self.wallets[0])
        print(st_)
        st, st_ = Wallet.print_transactions(self.wallets[0])
        print(st_)
        st, st_ = Wallet.print_operations(self.wallets[0])
        print(st_)
        
        for i in range(0, len(self.wallets)):
            state = Wallet.save_wallet(self.wallets[i], i)

            
