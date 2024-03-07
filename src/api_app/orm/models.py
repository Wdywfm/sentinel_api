from geoalchemy2 import Geometry
from sqlalchemy import JSON, BigInteger, Column, DateTime, String
from sqlalchemy.dialects.postgresql.types import BYTEA
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Image(Base):
    __tablename__ = "images"

    id = Column("id", BigInteger, autoincrement=True, primary_key=True)
    ref_polygon = Column(
        "ref_polygon",
        Geometry("POLYGON"),
        index=True,
        unique=True,
        comment="Reference polygon that was used to retrieve image from PYSTAC",
    )
    info = Column("info", JSON, comment="STAC API Item Search response")
    image = Column("image", BYTEA, comment="Satellite image of an area")
    date = Column("timestamp", DateTime(timezone=True))


class Field(Base):
    __tablename__ = "fields"

    id = Column("id", BigInteger, autoincrement=True, primary_key=True)
    name = Column("name", String, comment="Field name")
    polygon = Column("polygon", Geometry("POLYGON"), index=True)
