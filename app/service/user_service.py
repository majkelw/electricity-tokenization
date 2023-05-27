import base58

from utils.key_manager import KeyManager


class UserService:

    def __init__(self, core):
        self.core = core

    def create(self):
        user_id, private_key, words = KeyManager.generate_from_random_words()
        self.core.add_user(user_id)
        return 201, {"message": "Your wallet has been created, please save generated words in safe place",
                     "user_id": base58.b58encode(user_id),
                     "private_key": base58.b58encode(private_key),
                     "words": words}

    def recover(self, user_recovery_body):
        user_id, private_key = KeyManager.generate_from_input(user_recovery_body.words)
        return 200, {"message": "Key recovered from words",
                     "user_id": base58.b58encode(user_id),
                     "private_key": base58.b58encode(private_key)}

    def get_users_list(self):
        json_struct = []

        if self.core.users_id:
            for user in self.core.users_id:
                json_struct.append({base58.b58encode(user)})
        else:
            json_struct.append({"Any user exist."})

        return 200, json_struct

