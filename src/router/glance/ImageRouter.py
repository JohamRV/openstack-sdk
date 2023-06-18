from fastapi import APIRouter

router = APIRouter()

@router.get("", tags=["users"])
async def list_images():
    pass

@router.get()
async def show_image_detail():
    pass

async def import_image():
    pass

@router.delete()
async def delete_image():
    pass
