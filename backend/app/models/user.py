import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    clothes = relationship(
        "Clothing",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    events = relationship(
        "Event",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    outfits = relationship(
        "Outfit",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    preference = relationship(
        "Preference",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )