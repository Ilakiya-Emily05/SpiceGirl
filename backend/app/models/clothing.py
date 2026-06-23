import uuid

from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.db import Base


class Clothing(Base):
    __tablename__ = "clothes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    name = Column(String(100), nullable=False)

    category = Column(String(50), nullable=False)   # Top, Bottom, etc.

    color = Column(String(50), nullable=False)

    season = Column(String(50), nullable=False)

    style = Column(String(50), nullable=False)

    # 🔥 AI LAYER
    formality_score = Column(Float, default=0.5)  # 0 = casual, 1 = formal
    usage_count = Column(Float, default=0)        # implicit preference signal

    image_url = Column(String(500), nullable=True)

    user = relationship("User", back_populates="clothes")