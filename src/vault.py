import json


class Vault:
    def __init__(self):
        self._vault_file = "vault.json"

    def __repr__(self):
        return f"Vault()"

    def _get_records(self):
        with open(self._vault_file) as vault_file:
            vault_content = json.load(vault_file)
            records = [
                {
                    "url": record["url"],
                    "username": record["username"],
                    "password": record["password"],
                }
                for record in vault_content
            ]
            vault_file.close()
            return records

    def _record_exists(self, key) -> dict | None:
        for record in self._get_records():
            if record["url"] == key:
                return record
        return None

    def _update_vault(self, record: dict) -> None:
        with open(self._vault_file, "r+") as vault_file:
            content = json.load(vault_file)
            content.append(record)
            vault_file.seek(0)
            json.dump(content, vault_file)
            vault_file.close()
            # vault_file.write(json.dumps(self._vault_contents))

    def create_new_record(self, url: str, username: str, password: str):
        if not self._record_exists(url):
            new_entry = VaultRecord(url, username, password)
            with open(self._vault_file, "r+") as vault_file:
                content = json.load(vault_file)
                content.append(new_entry.__dict__)
                vault_file.seek(0)
                json.dump(content, vault_file)
                vault_file.close()
                print("New record created")
        else:
            print("Record already exists")
            yn = input("Do you want to overwrite it? (y/n): ")
            if yn == "y":
                self.update_record(url, username, password)

    def get_record(self, url: str):
        return self._record_exists(url)

    def update_record(self, url: str, username: str, password: str):
        records = self._get_records()
        for record in records:
            if record["url"] == url:
                record["username"] = username
                record["password"] = password

        with open(self._vault_file, "r+") as vault_file:
            vault_file.seek(0)
            json.dump(records, vault_file)
            vault_file.close()

        print("Record updated")


class VaultRecord:
    def __init__(self, url: str, username: str, password: str):
        self.url = url
        self.username = username
        self.password = password

    def __repr__(self):
        return (
            f"Vault(url={self.url}, username={self.username}, password={self.password})"
        )

    def __str__(self):
        return f"url: {self.url}, \nusername: {self.username}, \npassword: {self.password}\n"
