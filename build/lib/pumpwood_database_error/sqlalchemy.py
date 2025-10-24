"""Main module to treat SQLAlchemy errors."""
from loguru import logger
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from pumpwood_database_error.psycopg2 import TreatPsycopg2Error
from pumpwood_communication.exceptions import PumpWoodDatabaseError


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
        if isinstance(error, IntegrityError):
            return TreatPsycopg2Error.treat(
                error=error.orig, connection_url=connection_url)
        else:
            message = (
                "SQLAlchemy error [{erro_type}] not treated. "
                "Message:\n{message}")
            return_dict = PumpWoodDatabaseError(
                message=message,
                payload={
                    'erro_type': type(error).__name__,
                    'message': str(error)})\
                .to_dict()
            logger.warning(return_dict['message'])
            return return_dict
