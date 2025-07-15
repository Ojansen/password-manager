import os
from hashlib import pbkdf2_hmac


class Crypto:
    def __init__(self):
        self.iterations = 10_000
        self.encryption_algorithm = "sha256"

    def __repr__(self):
        return f"Crypto()"

    def pkc(self):
        salt = os.urandom(16)
        dk = pbkdf2_hmac(
            self.encryption_algorithm,
            self.get_master_password(),
            salt * 2,
            self.iterations,
        )
        return dk

    def create_new_secret(self) -> str:
        return self.pkc().hex()

    def set_master_password(self, master_password):
        pass

    def get_master_password(self) -> bytes:
        return b"Master password"
