import hashlib
import hmac

from mnemonic import Mnemonic


class KeyGenerator:
    mnemonic = Mnemonic("english")

    @classmethod
    def generate_from_input(cls, words):
        private_key = hmac.new(bytes(words, "utf-8"), digestmod=hashlib.sha256).digest()
        public_key = hashlib.sha256(private_key).digest()
        return private_key, public_key

    @classmethod
    def generate_from_random_words(cls):
        words = cls.mnemonic.generate(strength=256)
        private_key, public_key = cls.generate_from_input(words)
        return private_key, public_key, words
