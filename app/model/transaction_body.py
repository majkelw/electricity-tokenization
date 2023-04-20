from pydantic import BaseModel


class TransactionBody(BaseModel):
    from_user_id: str
    private_key: str
    to_user_id: str
