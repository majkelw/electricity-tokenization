from pydantic import BaseModel


class TokenDeletionBody(BaseModel):
    user_id: str
    amount: int
    energy_reception_code: str
