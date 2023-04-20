import base58

from app.utils.key_manager import KeyManager


class UserService:

    def create(self, core):
        user_id, private_key, words = KeyManager.generate_from_random_words()
        core.add_user(user_id)
        return 201, {"message": "Your wallet has been created, please save generated words in safe place",
                     "user_id": base58.b58encode(user_id),
                     "private_key": base58.b58encode(private_key),
                     "words": words}

    def recover(self, user_recovery_body):
        user_id, private_key = KeyManager.generate_from_input(user_recovery_body.words)
        return 200, {"message": "Key recovered from seed",
                     "user_id": user_id,
                     "private_key": base58.b58encode(private_key)}
