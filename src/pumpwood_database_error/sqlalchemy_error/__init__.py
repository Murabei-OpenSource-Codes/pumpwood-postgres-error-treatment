"""Auxiliary codes to treat expecific errors from sqlalchemy."""
from .unique_violation import TreatSQLAlchemyUniqueViolation

__docformat__ = "google"

__all__ = [
    TreatSQLAlchemyUniqueViolation, ]
