import uuid

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Table
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.db import Base


outfit_items = Table(
    "outfit_items",
    Base.metadata,

    Column(
        "outfit_id",
        UUID(as_uuid=True),
        ForeignKey("outfits.id"),
        primary_key=True
    ),

    Column(
        "clothing_id",
        UUID(as_uuid=True),
        ForeignKey("clothes.id"),
        primary_key=True
    )
)


class Outfit(Base):
    __tablename__ = "outfits"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    occasion = Column(
        String(100),
        nullable=False
    )

    score = Column(
        Integer,
        default=0
    )

    user = relationship(
        "User",
        back_populates="outfits"
    )

    clothes = relationship(
        "Clothing",
        secondary=outfit_items
    )