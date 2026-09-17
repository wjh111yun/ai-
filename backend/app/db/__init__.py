"""Database engine, sessions and migrations."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all application models."""
