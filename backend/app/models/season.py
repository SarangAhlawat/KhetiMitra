from sqlalchemy import Column, Integer, Text

from app.models.base import Base

class Season(Base):

    __tablename__ = "seasons"

    season_id = Column(Integer, primary_key=True)

    season_name = Column(Text)

    start_month = Column(Integer)

    end_month = Column(Integer)