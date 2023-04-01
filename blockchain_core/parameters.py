from enum import Enum

class InitializeOpt(Enum):
    BASED = 0
    SOURCE = 1
    
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

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

class Errors(Enum):
    STATE_OK = 0
    END_OF_BLOCKS = 1
    INCONSISTENT_POOL_PARAM = 2
    INCONSISTENT_HASH_LEN = 3

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

