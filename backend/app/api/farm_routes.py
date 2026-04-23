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
    payload = farm.dict()
    farm_size_acres = payload.get("farm_size_acres")
    if farm_size_acres is None:
        farm_size_acres = payload.get("farm_size")

    # Map request schema fields to actual ORM model columns.
    db_farm = Farm(
        farmer_id=payload["farmer_id"],
        farm_name=payload.get("farm_name"),
        farm_size_acres=farm_size_acres,
        soil_type=payload.get("soil_type"),
        irrigation_type=payload.get("irrigation_type"),
        water_source=payload.get("water_source")
    )

    db.add(db_farm)
    db.commit()
    db.refresh(db_farm)

    return db_farm