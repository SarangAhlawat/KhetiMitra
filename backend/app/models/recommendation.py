from sqlalchemy import Column, Integer, Float, Text, ForeignKey

from app.models.base import Base

class Recommendation(Base):

    __tablename__ = "recommendations"

    recommendation_id = Column(Integer, primary_key=True)

    farm_id = Column(
        Integer,
        ForeignKey("farms.farm_id")
    )

    recommended_crop = Column(Text)

    expected_yield = Column(Float)

    sustainability_score = Column(Float)

    confidence_score = Column(Float)

    recommendation_text = Column(Text)