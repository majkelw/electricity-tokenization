from enum import Enum
from typing import NamedTuple

class Transaction(NamedTuple):
    from_: str
    to_: str
    amount: int
    direction: str
    time: str
    
    HASH_LEN = 64
    
    TransactionStats = Enum('TransactionStats', ['STATE_OK', 'UNABLE_TO_CREATE', 'NONE_OBJ'])
    
    @classmethod
    def construct(self, from_, to_, amount, direction, time_):
        if (len(from_) == self.HASH_LEN and
            len(to_) == self.HASH_LEN and
            amount > 0):
            transaction = Transaction(from_, to_, amount, direction, time_)
            return (self.TransactionStats.STATE_OK, transaction)
        else:
            return (self.TransactionStats.UNABLE_TO_CREATE, None)
            
    @classmethod
    def print_transaction(self, transaction):
        if transaction != None:
            str_ = ""
            str_ = [transaction.from_[:3] + '...' + transaction.from_[-3:],
                    transaction.amount,
                    transaction.to_[:3] + '...' + transaction.to_[-3:],
                    transaction.direction,
                    transaction.time]
            return (self.TransactionStats.STATE_OK, str_)
        else:
            return (self.TransactionStats.NONE_OBJ, "")
