from typing import Optional

from pydantic import BaseModel


class FarmCreate(BaseModel):

    farmer_id: int
    farm_name: Optional[str] = None
    soil_type: str
    soil_ph: Optional[float] = None
    organic_carbon: Optional[float] = None
    farm_size: Optional[float] = None
    farm_size_acres: Optional[float] = None
    irrigation_type: str
    water_source: str
    gps_lat: Optional[float] = None
    gps_lon: Optional[float] = None