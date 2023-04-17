import datetime
import base58

from app.core.blockchain.pool import Pool, poolParam
from app.core.wallet.wallet import Wallet
from app.utils.key_generator import KeyGenerator


class UserService:
    users_id = []
    wallets = []
    HASH = '0000000000000000000000000000000000000000000000000000000000000000'

    def create(self, blockchain):
        while True:
            private_key, public_key, words = KeyGenerator.generate_from_random_words()
            if public_key not in self.users_id:
                break

        timestamp = datetime.datetime.now()
        state, wallet = Wallet.construct(public_key)
        Wallet.save_wallet(wallet, len(self.wallets))
        self.wallets.append(wallet)
        state, new_pool = Pool.construct(public_key, poolParam.nUSER.value, public_key, 1, str(timestamp), self.HASH)
        blockchain.add_pool(new_pool)
        self.users_id.append(public_key)

        return {"detail": "Your wallet has been created, please save generated words in safe place",
                "private_key": base58.b58encode(private_key), "public_key": base58.b58encode(public_key),
                "words": words}

    def recover_key(self, key_recovery_body):
        private_key, public_key = KeyGenerator.generate_from_input(key_recovery_body.words)
        return {"detail": "Key recovered from seed",
                "private_key": base58.b58encode(private_key),
                "public_key": base58.b58encode(public_key)}
