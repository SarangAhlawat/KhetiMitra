from app.core.database import engine

from app.models.base import Base

# Import models

import app.models.farmer
import app.models.farm
import app.models.season
import app.models.farm_history
import app.models.soil
import app.models.sustainability
import app.models.recommendation
import app.models.api_cache

def init_db():

    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":

    init_db()