"""seed_university_tables

Revision ID: 5e7d9c1b3a2f
Revises: None
Create Date: 2026-10-13 13:30:00.000000
"""
import csv
import os
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# Revision identifiers used by Alembic
revision = '5e7d9c1b3a2f'
down_revision = None  
branch_labels = None
depends_on = None

# ==============================================================================
# 1. Bulk Inserter Schema Targets (Used for data ingestion mapping)
# ==============================================================================
classroom_t = table('classroom', column('building', sa.String), column('room_number', sa.String), column('capacity', sa.Integer))
department_t = table('department', column('dept_name', sa.String), column('building', sa.String), column('budget', sa.Numeric))
course_t = table('course', column('course_id', sa.String), column('title', sa.String), column('dept_name', sa.String), column('credits', sa.Integer))
instructor_t = table('instructor', column('ID', sa.String), column('name', sa.String), column('dept_name', sa.String), column('salary', sa.Numeric))
time_slot_t = table('time_slot', column('time_slot_id', sa.String), column('day', sa.String), column('start_hr', sa.Integer), column('start_min', sa.Integer), column('end_hr', sa.Integer), column('end_min', sa.Integer))
section_t = table('section', column('course_id', sa.String), column('sec_id', sa.String), column('semester', sa.String), column('year', sa.Integer), column('building', sa.String), column('room_number', sa.String), column('time_slot_id', sa.String))
teaches_t = table('teaches', column('ID', sa.String), column('course_id', sa.String), column('sec_id', sa.String), column('semester', sa.String), column('year', sa.Integer))
student_t = table('student', column('ID', sa.String), column('name', sa.String), column('dept_name', sa.String), column('tot_cred', sa.Integer))
takes_t = table('takes', column('ID', sa.String), column('course_id', sa.String), column('sec_id', sa.String), column('semester', sa.String), column('year', sa.Integer), column('grade', sa.String))
advisor_t = table('advisor', column('s_ID', sa.String), column('i_ID', sa.String))
prereq_t = table('prereq', column('course_id', sa.String), column('prereq_id', sa.String))


def load_seed_file(file_name: str):
    """Helper to navigate outside 'src' to load raw data from 'resources/seeds'"""
    current_file_dir = os.path.dirname(__file__)
    api_workspace_root = os.path.abspath(os.path.join(current_file_dir, "..", "..", ".."))
    full_csv_path = os.path.join(api_workspace_root, 'resources', 'seeds', file_name)
    with open(full_csv_path, mode='r', encoding='utf-8-sig') as file:
        return list(csv.DictReader(file))


def upgrade():
    # ... [Keep your op.create_table blocks exactly as they are here] ...
    print("✨ Database tables built successfully.")

    # ==============================================================================
    # 2. Ingestion Phase (Wrapped with temporary constraint safety switches)
    # ==============================================================================
    print("🌱 Loading separated CSV entries into university database tables...")
    
    # Bypasses relational row sequence gaps during core loading
    op.execute(sa.text("SET FOREIGN_KEY_CHECKS = 0;"))
    
    op.bulk_insert(classroom_t, load_seed_file('classroom.csv'))
    print("✅ Classroom rows populated.")

    op.bulk_insert(department_t, load_seed_file('department.csv'))
    print("✅ Department rows populated.")

    op.bulk_insert(course_t, load_seed_file('course.csv'))
    print("✅ Course rows populated.")

    op.bulk_insert(instructor_t, load_seed_file('instructor.csv'))
    print("✅ Instructor rows populated.")

    op.bulk_insert(time_slot_t, load_seed_file('time_slot.csv'))
    print("✅ Time Slot rows populated.")

    op.bulk_insert(section_t, load_seed_file('section.csv'))
    print("✅ Section rows populated.")

    op.bulk_insert(teaches_t, load_seed_file('teaches.csv'))
    print("✅ Teaches rows populated.")

    op.bulk_insert(student_t, load_seed_file('student.csv'))
    print("✅ Student rows populated.")

    op.bulk_insert(takes_t, load_seed_file('takes.csv'))
    print("✅ Takes rows populated.")

    op.bulk_insert(advisor_t, load_seed_file('advisor.csv'))
    print("✅ Advisor rows populated.")

    op.bulk_insert(prereq_t, load_seed_file('prereq.csv'))
    print("✅ Prereq rows populated.")
    
    # Restore standard validation rules instantly
    op.execute(sa.text("SET FOREIGN_KEY_CHECKS = 1;"))
    print("🎉 All university records loaded flawlessly.")


def downgrade():
    print("🗑️ Wiping data rows and tables safely...")
    op.execute(sa.text("SET FOREIGN_KEY_CHECKS = 0;"))
    
    # List of all 11 tables to clean up
    tables_to_drop = [
        'prereq', 'advisor', 'takes', 'student', 'teaches', 
        'section', 'time_slot', 'instructor', 'course', 'department', 'classroom'
    ]
    
    # if_exists=True ensures it won't crash if the tables are already missing
    for tbl in tables_to_drop:
        op.drop_table(tbl, if_exists=True)
        
    op.execute(sa.text("SET FOREIGN_KEY_CHECKS = 1;"))
    print("❌ All university table structures cleared safely.")

