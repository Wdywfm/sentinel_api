import datetime

from sqlalchemy import func
from sqlalchemy.orm import Session

from api_app.orm import models
from api_app.orm.utils import geometry_to_wkt


class ImagesCRUD:
    @staticmethod
    def get_image_info_from_polygon(session: Session, polygon: dict) -> dict:
        """
        Returns image info from polygon if found, otherwise None
        :param session: sqlalchemy.orm.Session object
        :param polygon: (dict) input polygon
        :return: image info or None
        """
        image_info = (
            session.query(models.Image.info)
            .filter(func.ST_Equals(models.Image.ref_polygon, geometry_to_wkt(polygon)))
            .one_or_none()
        )

        return image_info if not image_info else image_info[0]

    @staticmethod
    def add_image_record(session: Session, ref_polygon: dict, image_info: dict) -> None:
        """
        Saves new Image record into the database
        :param session: sqlalchemy.orm.Session object
        :param ref_polygon: reference polygon
        :param image_info: STAC search response info
        :return: None
        """
        image_record = models.Image(
            ref_polygon=geometry_to_wkt(ref_polygon), info=image_info, date=datetime.datetime.utcnow()
        )
        session.add(image_record)
        session.commit()


class FieldsCRUD:
    @staticmethod
    def add_field_record(session: Session, polygon: dict, name: str) -> None:
        """
        Saves new Fields record into the database
        :param session: sqlalchemy.orm.Session object
        :param polygon: field polygon
        :param name: field name
        :return: None
        """
        field_record = models.Field(
            polygon=geometry_to_wkt(polygon),
            name=name,
        )
        session.add(field_record)
        session.commit()

    @staticmethod
    def query_fields(session: Session, polygon: dict) -> list:
        """
        Queries fields that intersect with the given polygon
        :param session: sqlalchemy.orm.Session object
        :param polygon: input polygon
        :return: list with field names
        """
        fields = (
            session.query(models.Field).filter(func.ST_Intersects(models.Field.polygon, geometry_to_wkt(polygon))).all()
        )
        return [field.name for field in fields]
