from fastapi import APIRouter

from api_app.routers import fields, images

router = APIRouter()


router.include_router(images.router, prefix="/images", tags=["images"])
router.include_router(fields.router, prefix="/fields", tags=["fields"])
