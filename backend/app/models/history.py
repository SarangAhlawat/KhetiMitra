from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from app.core.database import Base


class History(Base):

    __tablename__ = "farm_history"

    history_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    farm_id = Column(Integer)

    crop = Column(String)

    yield_value = Column(Float)

    fertilizer = Column(Float)

    pesticide = Column(Float)

    profit = Column(Float)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )