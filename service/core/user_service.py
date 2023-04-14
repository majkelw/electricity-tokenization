import hashlib
import hmac
import base58
from mnemonic import Mnemonic


class UserService:
    users_ids = ["001", "002", "003", "004"]
    mnemonic = Mnemonic("english")
    """
    mock na potrzeby symulatora, w tej klasie mozna zaimplementowac lub wywolac funkcje,
    ktora sprawdzi czy dany uzytkownik istnieje
    """

    def exist_by_id(self, user_id):
        return True if user_id in self.users_ids else False

    def create_user(self):
        words = self.mnemonic.generate(strength=256)
        private_key = hmac.new(bytes(words, "utf-8"), digestmod=hashlib.sha256).digest()
        public_key = hashlib.sha256(private_key).digest()
        return {"detail": "New user added, please save generated words in safe place",
                "private_key": base58.b58encode(private_key), "public_key": base58.b58encode(public_key),
                "words": words}
