from fastapi import APIRouter, UploadFile

from api_app.orm.connection import Session
from api_app.orm.crud import FieldsCRUD
from api_app.utils import get_geometry_from_polygon_file

router = APIRouter()


@router.post("/upload")
def store_field_data(file: UploadFile, name: str):
    """
    Store field in the database
    """
    field_polygon = get_geometry_from_polygon_file(file)
    with Session() as session:
        FieldsCRUD.add_field_record(session=session, polygon=field_polygon, name=name)
    return {"message": f"Field '{name}' has been successfully stored"}


@router.post("/query")
def query_fields(file: UploadFile):
    """
    Retrieve fields that intersect with the given polygon
    """
    polygon = get_geometry_from_polygon_file(file)
    with Session() as session:
        field_names = FieldsCRUD.query_fields(session=session, polygon=polygon)
    return {"message": field_names}
