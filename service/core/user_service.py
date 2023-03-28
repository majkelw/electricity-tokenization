class UserService:
    users_ids = ["001", "002", "003", "004"]
    """
    mock na potrzeby symulatora, w tej klasie mozna zaimplementowac lub wywolac funkcje,
    ktora sprawdzi czy dany uzytkownik istnieje
    """

    def exist_by_id(self, user_id):
        return True if user_id in self.users_ids else False
