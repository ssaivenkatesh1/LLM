from src.database import Base, engine
from src.models import models

print("Dropping all database tables...")
Base.metadata.drop_all(bind=engine)
print("Database tables dropped.")

print("Creating all database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created.")
