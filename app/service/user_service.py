import base58
from mnemonic import Mnemonic

from app.utils.key_generator import KeyGenerator


class UserService:
    users_ids = ["001", "002", "003", "004"]
    mnemonic = Mnemonic("english")
    """
    mock na potrzeby symulatora, w tej klasie mozna zaimplementowac lub wywolac funkcje,
    ktora sprawdzi czy dany uzytkownik istnieje
    """

    def exist_by_id(self, user_id):
        return True if user_id in self.users_ids else False

    def create(self):
        private_key, public_key, words = KeyGenerator.generate_from_random_words()
        return {"detail": "Successfully created, please save generated words in safe place",
                "private_key": base58.b58encode(private_key), "public_key": base58.b58encode(public_key),
                "words": words}

    def recover_key(self, key_recovery_body):
        private_key, public_key = KeyGenerator.generate_from_input(key_recovery_body.words)
        return {"detail": "Key recovered",
                "private_key": base58.b58encode(private_key), "public_key": base58.b58encode(public_key)}
