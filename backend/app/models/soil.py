from sqlalchemy import Column, Integer, Float, Date, ForeignKey

from app.models.base import Base

class SoilData(Base):

    __tablename__ = "soil_data"

    soil_id = Column(Integer, primary_key=True)

    farm_id = Column(
        Integer,
        ForeignKey("farms.farm_id")
    )

    sample_date = Column(Date)

    soil_pH = Column(Float)

    organic_carbon = Column(Float)

    nitrogen = Column(Float)

    phosphorus = Column(Float)

    potassium = Column(Float)

    moisture = Column(Float)