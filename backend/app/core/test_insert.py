from app.core.database import SessionLocal
from app.models.farmer import Farmer

db = SessionLocal()

farmer = Farmer(

    name="Test Farmer",

    phone="9999999999",

    language="Punjabi",

    district="Ludhiana",

    village="Village A"
)

db.add(farmer)

db.commit()

db.close()