import fastapi
import uvicorn

from model.energy_body import EnergyBody
from core.token_service import TokenService
from service.core.user_service import UserService

app = fastapi.FastAPI()
token_service = TokenService()
user_service = UserService()


@app.post("/create-token")
async def create_token(energy_body: EnergyBody):
    response_code, message = token_service.create_from(energy_body)
    if response_code != 200:
        raise fastapi.HTTPException(response_code, message)
    return {"detail": message}


@app.post("/create-user")
async def create_user():
    return user_service.create_user()


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
