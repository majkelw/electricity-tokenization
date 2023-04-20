class TokenService:

    def __convert_energy_to_tokens(self, energy_amount):
        return energy_amount / 2

    def __save(self, energy_body):
        return self.__convert_energy_to_tokens(energy_body.energy_amount)

    def create(self, energy_body):
        saved_tokens_number = self.__save(energy_body)
        return 201, {"message": f"Received {saved_tokens_number} tokens"}
