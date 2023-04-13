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
        return {"detail": "New user added, please save generated words in safe place",
                "words": self.mnemonic.generate(strength=256).split(" ")}
