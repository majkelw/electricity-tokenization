from typing import NamedTuple
from parameters import poolParam

class Pool(NamedTuple):
    id_1: str
    param: poolParam
    id_2: str
    amount: int
    time: str
    id_3: str

class Block(NamedTuple):
    beginHash: str
    endHash: str
    pools: list

class BlockChain(NamedTuple):
    blocks: list
