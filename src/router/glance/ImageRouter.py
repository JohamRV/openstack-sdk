from fastapi import APIRouter
from ...dao.glance.ImageDao import ImageDao
import os, dotenv

dotenv.load_dotenv("env/.env")
GLANCE_URL = os.getenv("OS_GLANCE_URL")
router = APIRouter(
    prefix="/glance",
    tags=["image"]
)
imageDao = ImageDao(GLANCE_URL, "gAAAAABkjyfoKeK6SmFEJ1U7TS1vMMWK8fMgetCKYQH26CaVt1aDMMdhbxpGzxw1QEvJhkHdwxPlrK8nsLd6DAQuug0pBN_zy_5eFIru6K9wzCZ8VD34CBalja1vH866Lw-iSoNoZ6_cC8fw0iPUfk8LTsG-eVUuRbiGAOnbrfqSmBXodvKp_2w")

@router.get("/image/list")
def list_images():
    res=imageDao.listImages()
    return res.json()

'''
@router.get()
def show_image_detail():
    pass

def import_image():
    pass

@router.delete()
def delete_image():
    pass
'''