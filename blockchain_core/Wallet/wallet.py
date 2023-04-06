from enum import Enum
from typing import NamedTuple
from prettytable import PrettyTable
import pickle
import datetime

from Wallet.transaction import Transaction
from Wallet.operation import Operation

class Wallet(NamedTuple):
    user_id: str
    bilance: list
    total_energy_consumpted: list
    total_energy_producted: list
    transactions: list
    operations: list
    
    DIR_TO_WALLETS = "../WALLETS/"
    FILE_NAME_PREF = "WALLET"
    
    WalletStats = Enum('WalletStats', ['STATE_OK', 'UNABLE_TO_CREATE', 'NEGATIVE_BILANCE', 'NEGATIVE_AMOUNT', 'UNABLE_TO_SAVE',
                                       'UNABLE_TO_OPEN', 'NOT_FOUND', 'NEGATIVE_ENERGY'])
    
    @classmethod
    def construct(self, user_id_):
        wallet = Wallet(user_id_, [0.0], [0.0], [0.0], [], [])
        return (self.WalletStats.STATE_OK, wallet)

    @classmethod
    def save_wallet(self, wallet, walletID):
        wallet_name = self.DIR_TO_WALLETS + self.FILE_NAME_PREF + str(walletID) + '.pkl'
        try: 
            with open(wallet_name, 'wb') as f:
                pickle.dump(wallet, f)
                f.close()
            return (self.WalletStats.STATE_OK)
        except IOError:
            return (self.WalletStats.UNABLE_TO_SAVE)
            
    @classmethod
    def read_wallet(self, walletID):
        wallet_name = self.DIR_TO_WALLETS + self.FILE_NAME_PREF + str(walletID) + '.pkl'
        try:
            with open(wallet_name, 'rb') as f:
                wallet = pickle.load(f)
                f.close()
            return (self.WalletStats.STATE_OK, wallet)
        except FileNotFoundError:
            return (self.WalletStats.NOT_FOUND, None)
        except IOError:
            return (self.WalletStats.UNABLE_TO_OPEN, None)
        
    @classmethod
    def add_amount(self, wallet, amount):
        if not amount < 0.0:
            wallet.bilance.append(amount)
            return (self.WalletStats.STATE_OK) 
        else:
            return (self.WalletStats.NEGATIVE_AMOUNT)

    @classmethod
    def add_energy_producted(self, wallet, energy):
        if not amount < 0.0:
            wallet.bilance.append(amount.total_energy_producted)
            return (self.WalletStats.STATE_OK) 
        else:
            return (self.WalletStats.NEGATIVE_ENERGY)

    @classmethod
    def add_energy_consumpted(self, wallet, energy):
        if not amount < 0.0:
            wallet.bilance.append(amount.total_energy_consumpted)
            return (self.WalletStats.STATE_OK) 
        else:
            return (self.WalletStats.NEGATIVE_ENERGY)
        
    @classmethod
    def remove_amount(self, wallet, amount):
        state = sum(wallet.bilance)
        
        if not state < amount: 
            if not amount < 0.0:
                wallet.bilance.append((-1.0) * amount)
                return (self.WalletStats.STATE_OK) 
            else:
                return (self.WalletStats.NEGATIVE_AMOUNT)
        else:
            return (self.WalletStats.NEGATIVE_BILANCE)
        
    @classmethod
    def add_transaction(self, wallet, transaction):
        wallet.transactions.append(transaction)
        return (self.WalletStats.STATE_OK)

    @classmethod
    def add_operation(self, wallet, operation):
        wallet.operations.append(operation)
        return (self.WalletStats.STATE_OK)
        
    @classmethod 
    def print_transactions(self, wallet):
        str_ = "" 

        x = PrettyTable()
        x.field_names = ["FROM", "AMOUNT", "TO", "DIRECTION", "TIME"]
        for transaction in wallet.transactions:
            state, transaction_st = Transaction.print_transaction(transaction)
            x.add_row(transaction_st)
        str_ += str(x)

        return (self.WalletStats.STATE_OK, str_)
        
    @classmethod 
    def print_operations(self, wallet):
        str_ = "" 

        x = PrettyTable()
        x.field_names = ["FROM", "AMOUNT", "TYPE", "TIME"]
        for operation in wallet.operations:
            state, operation_st = Operation.print_operation(operation)
            x.add_row(operation_st)
        str_ += str(x)

        return (self.WalletStats.STATE_OK, str_)
        
    @classmethod
    def print_status(self, wallet):
        str_ = "" 

        x = PrettyTable()
        x.field_names = ["ID", "BILANCE", "ENERGY CONSUMPTED", "ENERGY PRODUCTED", "TOTAL TRANSACTIONS", "TOTAL OPERATIONS"]
        x.add_row([wallet.user_id[:3] + '...' + wallet.user_id[-3:],
                   sum(wallet.bilance),
                   sum(wallet.total_energy_consumpted),
                   sum(wallet.total_energy_producted),
                   len(wallet.transactions),
                   len(wallet.operations)])
        str_ += str(x)

        return (self.WalletStats.STATE_OK, str_)
    

