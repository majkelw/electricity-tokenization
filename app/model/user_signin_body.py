from pydantic import BaseModel


class UserSigninBody(BaseModel):
    words: str
