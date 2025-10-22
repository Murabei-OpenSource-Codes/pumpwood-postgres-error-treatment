"""Main module to treat psycopg2 errors."""
import psycopg2
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from psycopg2.errors import (
    UniqueViolation, ForeignKeyViolation,
    NotNullViolation, CheckViolation,
    ExclusionViolation, RestrictViolation,
    TriggeredActionException)
from pumpwood_database_error.psycopg2_error import (
    TreatPsycopg2UniqueViolation, TreatPsycopg2CheckViolation,
    TreatPsycopg2ExclusionViolation, TreatPsycopg2ForeignKeyViolation,
    TreatPsycopg2NotNullViolation, TreatPsycopg2RestrictViolation,
    TreatPsycopg2TriggeredActionException)


class TreatPsycopg2Error:
    """Class to convert psycopg2 associated errors to normalized dictionary."""

    @classmethod
    def treat(cls, error: psycopg2.Error, connection_url: str = None) -> dict:
        """Main class to treat psycopg2 errors.

        Args:
            error (psycopg2.Error):
                Generic psycopg2 to be converted to dictionary.
            connection_url (str):
                Url for sqlalchemy.

        Returns:
            Return a dictionary with trteated error.
        """
        # Create the engine with NullPool
        engine = create_engine(connection_url, poolclass=NullPool)
        if isinstance(error, UniqueViolation):
            return TreatPsycopg2UniqueViolation.treat(
                error=error, engine=engine)

        elif isinstance(error, ForeignKeyViolation):
            return TreatPsycopg2ForeignKeyViolation.treat(
                error=error, engine=engine)

        elif isinstance(error, NotNullViolation):
            return TreatPsycopg2NotNullViolation.treat(
                error=error, engine=engine)

        elif isinstance(error, CheckViolation):
            return TreatPsycopg2CheckViolation.treat(
                error=error, engine=engine)

        elif isinstance(error, ExclusionViolation):
            return TreatPsycopg2ExclusionViolation.treat(
                error=error, engine=engine)

        elif isinstance(error, RestrictViolation):
            return TreatPsycopg2RestrictViolation.treat(
                error=error, engine=engine)

        elif isinstance(error, TriggeredActionException):
            return TreatPsycopg2TriggeredActionException.treat(
                error=error, engine=engine)

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
