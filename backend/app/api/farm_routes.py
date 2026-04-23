from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.farm import Farm
from app.schemas.farm_schema import FarmCreate


# router = APIRouter()
router = APIRouter(

    prefix="",

    tags=["Farm Management"]

)


@router.post("/farm")

def create_farm(

    farm: FarmCreate,
    db: Session = Depends(get_db)

):

    db_farm = Farm(**farm.dict())

    db.add(db_farm)
    db.commit()
    db.refresh(db_farm)

    return db_farm