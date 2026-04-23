from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.history import History
from app.schemas.history_schema import HistoryCreate


# router = APIRouter()
router = APIRouter(

    prefix="",

    tags=["Farm History"]

)


# Create history record

@router.post("/history")

def create_history(

    history: HistoryCreate,
    db: Session = Depends(get_db)

):

    db_history = History(
        farm_id=history.farm_id,
        crop=history.crop,
        yield_value=history.yield_value,
        fertilizer=history.fertilizer,
        pesticide=history.pesticide,
        profit=history.profit
    )

    db.add(db_history)

    db.commit()

    db.refresh(db_history)

    return db_history


# Get farm history

@router.get("/history/{farm_id}")

def get_history(

    farm_id: int,
    db: Session = Depends(get_db)

):

    records = db.query(History).filter(
        History.farm_id == farm_id
    ).all()

    return records