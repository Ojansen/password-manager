from crypto import Crypto
from vault import Vault


class Cli:
    def __init__(self):
        self.crypto = Crypto()
        self.vault = Vault()

    def __repr__(self):
        return f"Cli()"

    def run(self):
        print(
            """
            What would you like to do?
            1. Create a new password
            2. Create new record
            3. Find a record
            4. Update record
            q (Quit)
            """
        )
        while True:
            choice = input("Choose an option: ")

            match choice:
                case "1":
                    print(self.crypto.create_new_secret())
                case "2":
                    url = input("Enter URL: ")
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    self.vault.create_new_record(url, username, password)
                case "3":
                    url = input("Enter URL: ")
                    print(self.vault.get_record(url))
                case "4":
                    url = input("Enter URL: ")
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    self.vault.update_record(url, username, password)
                case _:
                    print("Thank you for using this program")
                    exit(0)
