from sqlalchemy import Integer, Text, DateTime, Float
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

# PrimeGen table
"""
PrimeGen Table
    - id (pk)
    - algo (str)
    - upperBound (int)
    - lowerBound (int)
    - timeElapsed (float)
    - primeLength (int)
    - result (str)
    - createdAt(datetime)
"""


class Base(DeclarativeBase):
    pass


class PrimeGen(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    algo: Mapped[str] = mapped_column("algo", Text, nullable=False)
    upperBound: Mapped[int] = mapped_column("upperBound", Integer)
    lowerBound: Mapped[int] = mapped_column("lowerBound", Integer)
    timeElapsed: Mapped[float] = mapped_column("timeElapsed", Float)
    primeLength: Mapped[int] = mapped_column("primeLength", Integer)
    result: Mapped[str] = mapped_column("result", Text, nullable=False)
    createdAt: Mapped[DateTime] = mapped_column(
        "createdAt", DateTime, default=datetime.utcnow
    )
