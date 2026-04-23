from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.farmer import Farmer
from app.schemas.farmer_schema import FarmerCreate


# router = APIRouter()
router = APIRouter(

    prefix="",

    tags=["Farmer Management"]

)


@router.post("/farmer")

def create_farmer(

    farmer: FarmerCreate,
    db: Session = Depends(get_db)

):

    db_farmer = Farmer(**farmer.dict())

    # # inside any route

    # raise Exception("Test error")

    db.add(db_farmer)
    db.commit()
    db.refresh(db_farmer)

    return db_farmer