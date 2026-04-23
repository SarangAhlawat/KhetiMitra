from app.core.database import engine
from app.models.qssm_record import Base

Base.metadata.create_all(bind=engine)

print("QSSM table created")