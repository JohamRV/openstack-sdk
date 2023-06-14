import os
import dotenv
from dao.keystone.AuthenticationDao import AuthenticationDao

class Login:
    def __init__(self) -> None:
        pass

    def main():
        dotenv.load_dotenv("./env/.env")
        while True:
            username = input("[.] Username: ")
            password = input("[.] Password: ")
            domain_id = os.getenv("OS_USER_DOMAIN_NAME")
            project_name = os.getenv("OS_PROJECT_NAME")
            base_url = os.getenv("OS_AUTH_URL")

            auth = AuthenticationDao(base_url)
            res = auth.passwordAuthentication(username, password, project_name, domain_id)

            if res.status_code == 201:
                print(f"\n[.] {username} is authenticate")
                #{"accessToken": res.headers["X-Subject-Token"], "userId": res.json()["token"]["user"]["id"]}

                break
            else:
                print("\n[.] Invalid credentials. Try again.\n")
                continue