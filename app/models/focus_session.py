from datetime import datetime
from .base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

class FocusSession(Base):
    __tablename__ = 'focus_sessions'

    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey('tasks.id'))
    start_time: Mapped[datetime] = mapped_column(default=datetime.now)
    end_time: Mapped[datetime] = mapped_column(nullable=True)
    duration: Mapped[int] = mapped_column(default=0)  # Duration in seconds
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)