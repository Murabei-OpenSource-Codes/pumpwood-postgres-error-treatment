"""Treat errors from ppsycopg2 and return them as normalized dictionaries."""
from .psycopg2 import TreatPsycopg2Error
from .sqlalchemy import TreatSQLAlchemyError

__docformat__ = "google"

__all__ = [TreatPsycopg2Error, TreatSQLAlchemyError]
