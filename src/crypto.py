import json
import os
from hashlib import pbkdf2_hmac


class Crypto:
    def __init__(self):
        self.iterations = 10_000
        self.encryption_algorithm = "sha256"
        self.salt = os.urandom(16)

    def __repr__(self):
        return f"Crypto()"

    @staticmethod
    def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
        return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

    def derive_key(self, password: str, salt: bytes) -> bytes:
        return pbkdf2_hmac(
            self.encryption_algorithm,
            password.encode(),
            salt,
            self.iterations,
            dklen=32,
        )

    def encrypt_vault(
        self, vault_data: dict, password: str, filename: str = "vault.enc"
    ):
        key = self.derive_key(password, self.salt)

        json_data = json.dumps(vault_data).encode()
        encrypted_data = self.xor_encrypt_decrypt(json_data, key)

        with open(filename, "wb") as f:
            f.write(self.salt + encrypted_data)

    def decrypt_vault(self, password: str, filename: str = "vault.enc") -> dict:
        with open(filename, "rb") as f:
            file_data = f.read()

        salt = file_data[:16]
        encrypted_data = file_data[16:]
        key = self.derive_key(password, salt)

        decrypted_data = self.xor_encrypt_decrypt(encrypted_data, key)
        return json.loads(decrypted_data.decode())
