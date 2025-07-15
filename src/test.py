from crypto import Crypto

crypto = Crypto()

vault = {"github.com": {"username": "devuser", "password": "hunter2"}}

mode = input("Encrypt or decrypt? (e/d): ")
password = input("Enter master password: ")

if mode == "e":
    crypto.encrypt_vault(vault, password)
    print("Vault encrypted and saved.")
else:
    try:
        data = crypto.decrypt_vault(password)
        print("Vault contents:", data)
    except Exception as e:
        print("Failed to decrypt:", e)
