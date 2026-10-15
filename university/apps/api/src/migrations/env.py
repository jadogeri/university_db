import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# 1. Force your 'src' folder onto the Python path so it can resolve internal imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# 2. Import your verified database configurations & metadata base
from configs.db import db_settings
from database import Base

# 3. Explicitly import ALL features so SQLAlchemy hooks them onto the metadata registry
from features.classroom.models import Classroom, TimeSlot
from features.department.models import Department, Instructor
from features.course.models import Course
from features.section.models import Section, Teaches
from features.student.models import Student, Takes, Advisor

# Access standard configuration properties
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 4. Bind the operational metadata schema target (Crucial for auto-generation)
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    # Use your Pydantic environment URL string instead of config ini selections
    url = db_settings.database_url
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # Fetch default configuration mapping dictionary
    configuration = config.get_section(config.config_ini_section) or {}
    
    # 5. Dynamic injection: Overwrite connection URL with your custom connection credentials
    configuration["sqlalchemy.url"] = db_settings.database_url

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
