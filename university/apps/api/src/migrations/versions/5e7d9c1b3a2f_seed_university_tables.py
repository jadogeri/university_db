"""seed_university_tables

Revision ID: 5e7d9c1b3a2f
Revises: <your_previous_structural_revision_id>
Create Date: 2026-10-13 13:30:00.000000
"""
import csv
import os
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# Revision identifiers used by Alembic
revision = '5e7d9c1b3a2f'
down_revision = '<your_previous_structural_revision_id>'
branch_labels = None
depends_on = None

# 1. Define table schema definitions for Alembic's query runner
permissions_table = table('permissions',
    column('id', sa.Integer),
    column('name', sa.String)
)

roles_table = table('roles',
    column('id', sa.Integer),
    column('name', sa.String)
)

users_table = table('users',
    column('id', sa.Integer),
    column('email', sa.String),
    column('full_name', sa.String),
    column('role_id', sa.Integer)
)

def load_seed_file(file_name: str):
    """Helper to navigate outside 'src' to load raw data from 'resources/seeds'"""
    current_file_dir = os.path.dirname(__file__)
    # Step up 3 levels out of src/ to the workspace root folder
    api_workspace_root = os.path.abspath(os.path.join(current_file_dir, "..", "..", ".."))
    full_csv_path = os.path.join(api_workspace_root, 'resources', 'seeds', file_name)
    
    with open(full_csv_path, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def upgrade():
    print("🌱 Loading separated CSV entries into database tables...")
    
    # Load and execute records sequentially to honor foreign key constraints
    permissions_data = load_seed_file('permissions.csv')
    op.bulk_insert(permissions_table, permissions_data)
    print("✅ Permissions rows populated.")

    roles_data = load_seed_file('roles.csv')
    op.bulk_insert(roles_table, roles_data)
    print("✅ Roles rows populated.")

    users_data = load_seed_file('users.csv')
    op.bulk_insert(users_table, users_data)
    print("✅ Users rows populated.")


def downgrade():
    print("🗑️ Wiping data rows in reverse relational order...")
    bind = op.get_bind()
    
    # Turn off constraint flags temporarily to bypass blockages during cleaning
    bind.execute(sa.text("SET FOREIGN_KEY_CHECKS = 0;"))
    
    bind.execute(users_table.delete())
    bind.execute(roles_table.delete())
    bind.execute(permissions_table.delete())
    
    bind.execute(sa.text("SET FOREIGN_KEY_CHECKS = 1;"))
    print("❌ All textbook data records removed cleanly.")
