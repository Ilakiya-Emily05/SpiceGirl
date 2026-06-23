import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.db import Base


class Clothing(Base):
    __tablename__ = "clothes"

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

    name = Column(
        String(100),
        nullable=False
    )

    category = Column(
        String(50),
        nullable=False
    )

    color = Column(
        String(50),
        nullable=False
    )

    season = Column(
        String(50),
        nullable=False
    )

    style = Column(
        String(50),
        nullable=False
    )

    image_url = Column(
        String(500),
        nullable=True
    )

    user = relationship(
        "User",
        back_populates="clothes"
    )