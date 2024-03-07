import json

from fastapi import APIRouter, UploadFile

from api_app.orm.connection import Session
from api_app.orm.crud import ImagesCRUD
from api_app.stac_manager import StacManager

router = APIRouter()


@router.post("/get")
def get_image(file: UploadFile):
    """
    Retrieve the newest image from a polygon
    """
    polygon = json.load(file.file)
    polygon = polygon["features"][0]["geometry"]
    with Session() as session:
        image_info = ImagesCRUD.get_image_info_from_polygon(session=session, polygon=polygon)
        if not image_info:
            stac_manager = StacManager()
            image_info = stac_manager.get_image_info_from_polygon(polygon=polygon)
            ImagesCRUD.add_image_record(session=session, ref_polygon=polygon, image_info=image_info)

    return {"message": image_info}  # Return image info for now, PNG can be constructed from assets in the future
