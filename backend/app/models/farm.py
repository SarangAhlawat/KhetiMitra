from sqlalchemy import Column, Integer, Float, Text, ForeignKey
from geoalchemy2 import Geography

from app.models.base import Base

class Farm(Base):

    __tablename__ = "farms"

    farm_id = Column(Integer, primary_key=True)

    farmer_id = Column(
        Integer,
        ForeignKey("farmers.farmer_id")
    )

    farm_name = Column(Text)

    farm_size_acres = Column(Float)

    soil_type = Column(Text)

    irrigation_type = Column(Text)

    water_source = Column(Text)

    gps_location = Column(
        Geography("POINT")
    )