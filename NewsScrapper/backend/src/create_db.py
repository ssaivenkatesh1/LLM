from src.database import Base, engine
from src.models import models

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created.")
