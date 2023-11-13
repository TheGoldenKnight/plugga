
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    total_time: Mapped[int]
    week_time: Mapped[int]
    day_time: Mapped[float]
    missed_days: Mapped[int]
    challange_accepted: Mapped[bool]
    period_failed: Mapped[int]
    deleted: Mapped[bool]
    day_overtime: Mapped[int]


class Date(Base):
    __tablename__ = "dates"
    id: Mapped[int] = mapped_column(primary_key=True)
    start_date: Mapped[str]
    end_date: Mapped[str]
    period: Mapped[int]
