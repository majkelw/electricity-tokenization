from utils.key_manager import KeyManager


class UserService:

    def __init__(self, core):
        self.core = core

    def create(self):
        user_id, private_key, words = KeyManager.generate_from_random_words()
        self.core.add_user(user_id)
        return 201, {"message": "Konto zostało utworzone",
                     "user_id": user_id,
                     "private_key": private_key,
                     "words": words}

    def signin(self, user_recovery_body):
        user_id, private_key = KeyManager.generate_from_input(user_recovery_body.words)
        if user_id in self.core.users_id:
            return 200, {"message": "Zalogowano",
                         "user_id": user_id,
                         "private_key": private_key}
        return 401, {"message": "Logowanie nie powiodło się"}

    def get_users_list(self):
        json_struct = []
        for user in self.core.users_id:
            json_struct.append({"user_id": user})

        return 200, json_struct
