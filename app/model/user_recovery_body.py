from pydantic import BaseModel


class UserRecoveryBody(BaseModel):
    words: str
