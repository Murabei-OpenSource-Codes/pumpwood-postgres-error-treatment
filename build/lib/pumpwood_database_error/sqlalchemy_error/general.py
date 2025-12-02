"""Main module to treat psycopg2 errors."""
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.exc import SQLAlchemyError
from pumpwood_database_error.sqlalchemy_error.not_found import (
    TreatSQLAlchemyNoResultFound)

# Use psycopg2 class to treat SQLAlchemy errors from psycopg2
from pumpwood_database_error.psycopg2_error import TreatPsycopg2Error
from pumpwood_database_error.abc import ErrorTreatmentABC


class TreatSQLAlchemyError(ErrorTreatmentABC):
    """Class to convert sqlalchemy associated errors to normalized dict."""

    @classmethod
    def can_treat(cls, error: Exception) -> bool:
        """Check if error is of the type treated by this class.

        Returns:
            Returns true if error is of the class treated by this class.
        """
        return isinstance(error, SQLAlchemyError)

    @classmethod
    def treat(cls, error: SQLAlchemyError, connection_url: str) -> dict:
        """Main class to treat psycopg2 errors.

        Args:
            error (psycopg2.Error):
                Generic psycopg2 to be converted to dictionary.
            connection_url (Engine):
                Connection URL for SQLAlchemy.

        Returns:
            Return a dictionary with treeated error.
        """
        if not cls.can_treat(error=error):
            msg = (
                "Error [{error_name}] can not be treated by "
                "TreatPsycopg2Error")\
                .format(error_name=error.__class__.__name__)
            raise Exception(msg)

        # Create the engine with NullPool
        engine = create_engine(connection_url, poolclass=NullPool)
        if TreatSQLAlchemyNoResultFound.can_treat(error):
            return TreatSQLAlchemyNoResultFound\
                .treat(error=error, engine=engine)

        # Check if error is from Psycopg2, if so treat it using a expecilised
        # class.
        if TreatPsycopg2Error.can_treat(error.orig):
            return TreatPsycopg2Error\
                .treat(error=error.orig, engine=engine)

        else:
            message = (
                "SQLAlchemy error [{erro_type}] not treated. "
                "Message:\n{message}")\
                .format(
                    erro_type=type(error).__name__,
                    message=str(error))
            logger.warning(message)
            return {
                "type": "PumpWoodDatabaseError",
                "message": message,
                "payload": {
                    'erro_type': type(error).__name__,
                    'message': str(error)
                }
            }
