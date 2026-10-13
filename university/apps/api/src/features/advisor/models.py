from typing import Optional
from sqlalchemy import String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from src.constants import TableNames

class Advisor(Base):
    __tablename__ = TableNames.ADVISOR

    s_id: Mapped[str] = mapped_column("s_ID", String(5), ForeignKey(f"{TableNames.STUDENT}.ID", ondelete="CASCADE"), primary_key=True)
    i_id: Mapped[Optional[str]] = mapped_column("i_ID", String(5), ForeignKey(f"{TableNames.INSTRUCTOR}.ID", ondelete="SET NULL"))

    __table_args__ = (PrimaryKeyConstraint("s_ID"),)
