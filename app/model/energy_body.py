from pydantic import BaseModel


class EnergyBody(BaseModel):
    user_id: str
