import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.db import Base


class Preference(Base):
    __tablename__ = "preferences"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    favorite_color = Column(
        String(50),
        nullable=True
    )

    favorite_style = Column(
        String(50),
        nullable=True
    )

    user = relationship(
        "User",
        back_populates="preference"
    )