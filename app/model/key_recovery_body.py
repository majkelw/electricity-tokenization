from pydantic import BaseModel


class KeyRecoveryBody(BaseModel):
    words: str
