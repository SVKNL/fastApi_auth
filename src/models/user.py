
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, created_at, intpk


class User(Base):
    __tablename__ = 'user'

    id: Mapped[intpk]
    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False)
    email: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        unique=True)
    created_at: Mapped[created_at]

    watched_tasks: Mapped[list['Task']] = relationship(
        'Task',
        secondary='task_watchers',
        back_populates='watchers',
    )
    executed_tasks: Mapped[list['Task']] = relationship(
        'Task',
        secondary='task_executors',
        back_populates='executors',
    )
