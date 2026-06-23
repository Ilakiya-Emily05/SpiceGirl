import uuid

from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.db import Base


class Preference(Base):
    __tablename__ = "preferences"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)

    # 🔥 AI MEMORY WEIGHTS
    favorite_color = Column(String(50), nullable=True)
    favorite_style = Column(String(50), nullable=True)

    # REAL AI SIGNALS
    color_weight = Column(Float, default=1.0)
    style_weight = Column(Float, default=1.0)

    # behavioral learning
    formal_bias = Column(Float, default=0.5)  # learns if user prefers formal/casual

    user = relationship("User", back_populates="preference")