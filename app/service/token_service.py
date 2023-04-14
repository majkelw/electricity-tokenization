from app.service.user_service import UserService


class TokenService:
    user_service = UserService()

    """
    mock na potrzeby symulatora, w tej klasie mozna zaimplementowac lub wywolac funkcje,
    ktora przeliczy energie na liczbe tokenów i zapisze je w blockchainie
    """

    def __convert_energy_to_tokens(self, energy_amount):
        return energy_amount / 2

    def __save(self, energy_body):  # zapisanie tokena w blockchain
        return self.__convert_energy_to_tokens(energy_body.energy_amount)

    # zwracamy kod i wiadomosc dla uzytkownika
    def create(self, energy_body):
        if not self.user_service.exist_by_id(energy_body.user_id):
            return 401, "User does not exist"
        saved_tokens_num = self.__save(energy_body)
        return 200, f"Received {saved_tokens_num} tokens"
