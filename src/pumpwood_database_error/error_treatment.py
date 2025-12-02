"""Main module to treat SQLAlchemy errors."""
from loguru import logger
from pumpwood_communication.exceptions import PumpWoodDatabaseError

# Load general error treatment
from pumpwood_database_error.psycopg2_error import TreatPsycopg2Error
from pumpwood_database_error.sqlalchemy_error import TreatSQLAlchemyError


class TreatPumpwoodError:
    """Centralize error treatment for SQLAlchemy and Psycopg2."""

    @classmethod
    def treat(cls, error: Exception, connection_url: str) -> dict:
        """Main class to treat SQLAlchemy errors.

        Args:
            error (psycopg2.Error):
                Generic SQLAlchemy to be converted to dictionary.
            connection_url (str):
                Conenction URL to connect with SQLAlchemy.

        Returns:
            Return a dictionary with
        """
        if TreatSQLAlchemyError.can_treat(error=error):
            return TreatSQLAlchemyError.treat(
                error=error, connection_url=connection_url)
        if TreatPsycopg2Error.can_treat(error=error):
            return TreatPsycopg2Error.treat(
                error=error, connection_url=connection_url)
        else:
            message = (
                "Error [{erro_type}] not treated. "
                "Message:\n{message}")
            return_dict = PumpWoodDatabaseError(
                message=message,
                payload={
                    'erro_type': type(error).__name__,
                    'message': str(error)})\
                .to_dict()
            logger.warning(return_dict['message'])
            return return_dict
