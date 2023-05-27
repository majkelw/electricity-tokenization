from pydantic import BaseModel


class TransactionBody(BaseModel):
    id_from: str
    id_to: str
    amount: str
