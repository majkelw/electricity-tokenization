from pydantic import BaseModel


class TransactionBody(BaseModel):
    user_id_from: str
    user_id_to: str
    amount: str
