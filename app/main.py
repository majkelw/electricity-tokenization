import uvicorn
from fastapi import FastAPI, Response

from model.transaction_body import TransactionBody
from model.user_recovery_body import UserRecoveryBody
from service.transaction_service import TransactionService
from service.user_service import UserService
from model.energy_body import EnergyBody
from service.token_service import TokenService
from core.core import Core

app = FastAPI()
core = Core()
core.contruct_wallets()
token_service = TokenService(core)
user_service = UserService(core)
transaction_service = TransactionService(core)


@app.post("/tokens")
async def create_token(energy_body: EnergyBody, response: Response):
    response_code, response_body = token_service.create(energy_body)
    response.status_code = response_code
    return response_body


@app.post("/users")
async def create_user():
    response_code, response_body = user_service.create()
    return response_body
    

@app.post("/users/recover")
async def recover_user(user_recovery_body: UserRecoveryBody):
    response_code, response_body = user_service.recover(user_recovery_body)
    return response_body


@app.post("/transactions")
async def verify_user(transaction_body: TransactionBody, response: Response):
    response_code, response_body = transaction_service.create(transaction_body)
    response.status_code = response_code
    return response_body


@app.get("/blockchain")
async def get_blockchain():
    return core.blockchain.to_json()


@app.get("/wallet")
async def get_wallet(coded_user_id: str):
    return core.wallet_to_json(coded_user_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
    #uvicorn.run(app, port=8080)

