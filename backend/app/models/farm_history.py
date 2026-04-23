from sqlalchemy import Column, Integer, Float, Text, ForeignKey

from app.models.base import Base

class FarmHistory(Base):

    __tablename__ = "farm_history"

    history_id = Column(Integer, primary_key=True)

    farm_id = Column(
        Integer,
        ForeignKey("farms.farm_id")
    )

    season_id = Column(
        Integer,
        ForeignKey("seasons.season_id")
    )

    year = Column(Integer)

    crop = Column(Text)

    yield_kg_per_ha = Column(Float)

    fertilizer_used = Column(Float)

    pesticide_used = Column(Float)

    irrigation_used = Column(Float)

    production_cost = Column(Float)

    profit = Column(Float)