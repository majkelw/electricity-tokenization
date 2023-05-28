import hashlib
import random

from core.core import Core
from datetime import datetime, timedelta


class TokenService:
    RECEPTION_CODE_DURATION_SECONDS = 10
    energy_reception_codes_data = []

    def __init__(self, core):
        self.core = core

    def create(self, energy_body):
        random_bits = random.getrandbits(128)
        token = hashlib.sha256(str(random_bits).encode('utf-8')).hexdigest()
        if self.core.add_token(token, energy_body.user_id) == Core.CoreStats.USER_NOT_EXIST:
            return 400, {"message": "Taki użytkownik nie istnieje, nie udało się utworzyc tokena"}
        return 201, {"message": "Utworzono token"}

    def generate_reception_code(self, energy_body):
        energy_reception_codes = [data['reception_code'] for data in self.energy_reception_codes_data]
        while True:
            generated_energy_reception_code = random.randint(100000, 999999)
            if generated_energy_reception_code not in energy_reception_codes:
                break

        end_datetime = datetime.today() + timedelta(seconds=self.RECEPTION_CODE_DURATION_SECONDS)
        self.energy_reception_codes_data.append(
            {"user_id": energy_body.user_id, "energy_reception_code": generated_energy_reception_code,
             "end_datetime": end_datetime})
        return 201, {"energy_reception_code": generated_energy_reception_code, "message": "Wygenerowano kod"}

    def remove_expired_reception_codes(self):
        for energy_reception_code_data in self.energy_reception_codes_data:
            if datetime.today() >= energy_reception_code_data["end_datetime"]:
                self.energy_reception_codes_data.remove(energy_reception_code_data)
