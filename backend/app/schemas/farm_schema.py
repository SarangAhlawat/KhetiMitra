from pydantic import BaseModel


class FarmCreate(BaseModel):

    farmer_id: int
    soil_type: str
    soil_ph: float
    organic_carbon: float
    farm_size: float
    irrigation_type: str
    water_source: str
    gps_lat: float
    gps_lon: float