from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    # After migration v4 (renamed from 'name' -> 'full_name')
    full_name = Column(String, nullable=False)

    # After migration v5 (unique constraint added)
    email = Column(String, nullable=False, unique=True, index=True)

    # Added in migration v2
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Added in migration v6 (data migration split)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)

    # Relationship
    projects = relationship("Project", back_populates="user", cascade="all, delete")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="projects")
