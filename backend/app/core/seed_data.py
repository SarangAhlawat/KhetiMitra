from app.core.database import SessionLocal
from app.models.season import Season

db = SessionLocal()

seasons = [

    Season(
        season_name="Kharif",
        start_month=6,
        end_month=10
    ),

    Season(
        season_name="Rabi",
        start_month=10,
        end_month=3
    ),

    Season(
        season_name="Zaid",
        start_month=3,
        end_month=6
    )
]

db.add_all(seasons)

db.commit()

db.close()