import fastapi
import uvicorn

from model.energy_body import EnergyBody
from service.token_service import TokenService
from app.service.user_service import UserService
from app.model.key_recovery_body import KeyRecoveryBody

app = fastapi.FastAPI()
token_service = TokenService()
user_service = UserService()


@app.post("/create-token")
async def create_token(energy_body: EnergyBody):
    response_code, message = token_service.create(energy_body)
    if response_code != 200:
        raise fastapi.HTTPException(response_code, message)
    return {"detail": message}


@app.post("/create-user")
async def create_user():
    return user_service.create()


@app.post("/recover-key")
async def recover_key(key_recovery_body: KeyRecoveryBody):
    return user_service.recover_key(key_recovery_body)


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
