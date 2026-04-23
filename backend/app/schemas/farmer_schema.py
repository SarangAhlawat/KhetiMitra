from pydantic import BaseModel


class FarmerCreate(BaseModel):

    name: str
    phone: str
    district: str
    village: str
    language: str


class FarmerResponse(BaseModel):

    farmer_id: int
    name: str
    phone: str
    district: str
    village: str
    language: str

    class Config:
        from_attributes = True