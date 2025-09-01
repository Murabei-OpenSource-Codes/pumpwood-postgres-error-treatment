"""Main module to treat SQLAlchemy errors."""
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from pumpwood_database_error.sqlalchemy_error import (
    TreatSQLAlchemyUniqueViolation)


class TreatSQLAlchemyError:
    """Class to convert SQLAlchemy associated errors to normalized dict."""

    @classmethod
    def treat(cls, error: SQLAlchemyError, connection_url: str) -> dict:
        """Main class to treat SQLAlchemy errors.

        Args:
            error (psycopg2.Error):
                Generic SQLAlchemy to be converted to dictionary.
            connection_url (str):
                Conenction URL to connect with SQLAlchemy.

        Returns:
            Return a dictionary with
        """
        # Create the engine with NullPool
        engine = create_engine(connection_url, poolclass=NullPool)

        if isinstance(error, IntegrityError):
            return TreatSQLAlchemyUniqueViolation.treat(
                error=error, engine=engine)
        else:
            message = str(error)
            print("not treated:", message)
            return {
                "message": message,
                "type": "PumpWoodDatabaseError",
                "payload": {}
            }
