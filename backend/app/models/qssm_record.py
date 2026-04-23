from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer

from app.core.database import Base


class QSSMRecord(Base):

    __tablename__ = "qssm_scores"

    id = Column(
        Integer,
        primary_key=True
    )

    farm_id = Column(
        Integer
    )

    qssm_score = Column(
        Float
    )