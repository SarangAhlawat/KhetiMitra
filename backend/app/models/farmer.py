from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func

from app.models.base import Base

class Farmer(Base):

    __tablename__ = "farmers"

    farmer_id = Column(Integer, primary_key=True)

    name = Column(Text, nullable=False)

    phone = Column(String, unique=True)

    language = Column(String)

    district = Column(String)

    village = Column(String)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )