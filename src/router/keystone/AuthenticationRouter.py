from fastapi import APIRouter
from ...dao.keystone.AuthenticationDao import AuthenticationDao
from ...model.Credential import Credential
import os, dotenv

dotenv.load_dotenv("env/.env")
KEYSTONE_URL = os.getenv("OS_AUTH_URL")
DOMAIN_ID = os.getenv("OS_USER_DOMAIN_NAME")
PROJECT_NAME = os.getenv("OS_PROJECT_NAME")

authenticationDao = AuthenticationDao(KEYSTONE_URL)

router = APIRouter(
    prefix="/keystone/auth",
    tags=["auth"]
)

@router.post("/password")
def password_authentication(credential: Credential):
    response=authenticationDao.passwordAuthentication(
        credential.username,
        credential.password,
        PROJECT_NAME,
        DOMAIN_ID
    )
    print(response)
    return {"message":"OK"}