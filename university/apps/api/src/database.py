# apps/api/src/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from configs.db import db_settings as settings

# 1. Pull the connection string dynamically from your secure Pydantic environment configurations
DATABASE_URL = settings.database_url

# 2. Configure the production-ready SQLAlchemy Database Engine.
# Adding pool_pre_ping=True prevents MySQL timeout crashes by automatically verifying 
# that idle socket tunnels are active before processing incoming requests.
engine = create_engine(
    DATABASE_URL, 
    pool_pre_ping=True,
    pool_recycle=3600,  # Explicitly recycles active connections every hour
    echo=False          # Toggle to True if you want to stream the raw SQL logs to your terminal
)

# 3. Establish the foundational session maker framework
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# 4. Define the central Core Declarative Base.
# Every single one of your 11 split feature model entities will inherit from this class 
# so Alembic can track their structural metadata variations uniformly.
class Base(DeclarativeBase):
    pass


# 5. Dependency injection generator function to manage the lifecycle of your sessions.
# This ensures every incoming HTTP request gets an isolated database link transaction context, 
# and securely commits or teardown resources automatically after execution.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        # Guarantees the database socket returns cleanly to the connection pool 
        # even if an unexpected error occurs inside your service layers.
        db.close()
