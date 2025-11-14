"""Treat errors from sqlalchemy and psycopg2 and return on dictionary."""
from .error_treatment import TreatPumpwoodError
from pumpwood_database_error.psycopg2_error import TreatPsycopg2Error
from pumpwood_database_error.sqlalchemy_error import TreatSQLAlchemyError

__all__ = [
    TreatPumpwoodError,
    TreatPsycopg2Error,
    TreatSQLAlchemyError
]


__docformat__ = "google"
