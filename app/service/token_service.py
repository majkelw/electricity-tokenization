import hashlib
import random

from core.core import Core


class TokenService:

    def __init__(self, core):
        self.core = core

    def create(self, energy_body):

        random_bits = random.getrandbits(128)
        token = hashlib.sha256(str(random_bits).encode('utf-8')).hexdigest()
        if self.core.add_token(token, energy_body.user_id) == Core.CoreStats.USER_NOT_EXIST:
            return 400, {"message": "Unable to create token, user does not exist"}

        return 201, {"message": "Token was created"}
