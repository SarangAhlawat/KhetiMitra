from sqlalchemy import Column, Integer, Text, JSON

from app.models.base import Base

class APICache(Base):

    __tablename__ = "api_cache"

    cache_id = Column(Integer, primary_key=True)

    api_name = Column(Text)

    request_hash = Column(Text)

    response_json = Column(JSON)