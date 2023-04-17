from enum import Enum
from typing import NamedTuple

class Operation(NamedTuple):
    from_: str
    amount: float
    op_type: str
    time: str
    
    HASH_LEN = 64
    
    OperationStats = Enum('OperationStats', ['STATE_OK', 'UNABLE_TO_CREATE', 'NONE_OBJ'])
    
    @classmethod
    def construct(self, from_, amount, op_type, time):
        if (len(from_) == self.HASH_LEN and
            amount > 0.0):
            operation = Operation(from_, amount, op_type, time)
            return (self.OperationStats.STATE_OK, operation)
        else:
            return (self.OperationStats.UNABLE_TO_CREATE, None)
            
    @classmethod
    def print_operation(self, operation):
        if operation != None:
            str_ = ""
            str_ = [operation.from_[:3] + '...' + operation.from_[-3:],
                    operation.amount,
                    operation.op_type,
                    operation.time]
            return (self.OperationStats.STATE_OK, str_)
        else:
            return (self.OperationStats.NONE_OBJ, "")
