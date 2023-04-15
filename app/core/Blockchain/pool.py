from enum import Enum
from typing import NamedTuple

class poolParam(Enum):
    SEND = 0
    nTOKEN = 1
    dTOKEN = 2
    nUSER = 3
    dUSER = 4
    NOTHING = 5
    
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

class Pool(NamedTuple):
    id_1: str
    param: poolParam
    id_2: str
    amount: int
    time: str
    id_3: str

    HASH_LEN = 64

    PoolStats = Enum('PoolStats', ['STATE_OK', 'NONE_OBJ', 'INCONSISTENT_POOL_PARAM', 'INCONSISTENT_HASH_LEN'])

    @classmethod
    def construct(self, id_1_, param_, id_2_, amount_, time_, id_3_):
        if (poolParam.has_value(param_)):
            if (len(id_1_) == self.HASH_LEN and
                len(id_2_) == self.HASH_LEN and
                len(id_3_) == self.HASH_LEN):
                pool = Pool(id_1_, param_, id_2_, amount_, time_, id_3_)
                return (self.PoolStats.STATE_OK, pool)
            else:
                return (self.PoolStats.INCONSISTENT_HASH_LEN, None)
        else:
            return (self.PoolStats.INCONSISTENT_POOL_PARAM, None)

    @classmethod
    def print_pool(self, pool):
        if pool != None:
            str_ = ""
            str_ = [pool.id_1[:3] + '...' + pool.id_1[-3:],
                    pool.param,
                    pool.id_2[:3] + '...' + pool.id_2[-3:],
                    str(pool.amount),
                    pool.time,
                    pool.id_3[:3] + '...' + pool.id_3[-3:]]
            return (self.PoolStats.STATE_OK, str_)
        else:
            return (self.PoolStats.NONE_OBJ, "")

