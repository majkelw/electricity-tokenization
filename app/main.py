import time
from threading import Thread

import uvicorn
import socket
from fastapi import FastAPI, Response

from model.token_deletion_body import TokenDeletionBody
from model.transaction_body import TransactionBody
from model.user_id_body import UserIdBody
from model.user_signin_body import UserSigninBody
from service.transaction_service import TransactionService
from service.user_service import UserService
from service.token_service import TokenService
from core.core import Core

app = FastAPI()
core = Core()
core.contruct_wallets()
token_service = TokenService(core)
user_service = UserService(core)
transaction_service = TransactionService(core)


@app.post("/tokens")
async def create_token(user_id_body: UserIdBody, response: Response):
    response_code, response_body = token_service.create(user_id_body)
    response.status_code = response_code
    return response_body


@app.delete("/tokens")
async def create_token(token_deletion_body: TokenDeletionBody, response: Response):
    response_code, response_body = token_service.delete(token_deletion_body)
    response.status_code = response_code
    return response_body


@app.post("/tokens/reception-code")
async def create_token(user_id_body: UserIdBody, response: Response):
    response_code, response_body = token_service.generate_reception_code(user_id_body)
    response.status_code = response_code
    return response_body


@app.get("/users")
async def get_users(response: Response):
    response_code, response_body = user_service.get_users_list()
    response.status_code = response_code
    return response_body


@app.post("/users/signup")
async def signup(response: Response):
    response_code, response_body = user_service.create()
    response.status_code = response_code
    print(response_body)
    return response_body


@app.post("/users/signin")
async def signin(user_signin_body: UserSigninBody, response: Response):
    response_code, response_body = user_service.signin(user_signin_body)
    response.status_code = response_code
    return response_body


@app.post("/transactions")
async def make_transaction(transaction_body: TransactionBody, response: Response):
    response_code, response_body = transaction_service.create(transaction_body)
    response.status_code = response_code
    return response_body


@app.get("/blockchain")
async def get_blockchain():
    return core.blockchain.to_json()


@app.get("/wallet")
async def get_wallet(user_id: str):
    return core.wallet_to_json(user_id)


def schedule_reception_codes_remover():
    while True:
        token_service.remove_expired_reception_codes()
        time.sleep(1)


if __name__ == "__main__":
    thread = Thread(target=schedule_reception_codes_remover)
    thread.start()
    uvicorn.run(app, host=socket.gethostbyname_ex(socket.getfqdn())[2][1], port=8080)
