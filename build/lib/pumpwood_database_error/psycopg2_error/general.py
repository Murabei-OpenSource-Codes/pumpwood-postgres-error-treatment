"""Main module to treat psycopg2 errors."""
import psycopg2
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from pumpwood_database_error.abc import ErrorTreatmentABC
from pumpwood_database_error.psycopg2_error.check_violation import (
    TreatPsycopg2CheckViolation)
from pumpwood_database_error.psycopg2_error.exclusion_violation import (
    TreatPsycopg2ExclusionViolation)
from pumpwood_database_error.psycopg2_error.foreignkey_violation import (
    TreatPsycopg2ForeignKeyViolation)
from pumpwood_database_error.psycopg2_error.notnull_violation import (
    TreatPsycopg2NotNullViolation)
from pumpwood_database_error.psycopg2_error.restrict_violation import (
    TreatPsycopg2RestrictViolation)
from pumpwood_database_error.psycopg2_error.triggered_action_exception import (
    TreatPsycopg2TriggeredActionException)
from pumpwood_database_error.psycopg2_error.unique_violation import (
    TreatPsycopg2UniqueViolation)


class TreatPsycopg2Error(ErrorTreatmentABC):
    """Class to convert psycopg2 associated errors to normalized dictionary."""

    @classmethod
    def can_treat(cls, error: Exception) -> bool:
        """Check if error is of the type treated by this class.

        Returns:
            Returns true if error is of the class treated by this class.
        """
        return isinstance(error, psycopg2.Error)

    @classmethod
    def treat(cls, error: psycopg2.Error, connection_url: str) -> dict:
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
        if TreatPsycopg2UniqueViolation.can_treat(error=error):
            return TreatPsycopg2UniqueViolation\
                .treat(error=error, engine=engine)

        if TreatPsycopg2ForeignKeyViolation.can_treat(error=error):
            return TreatPsycopg2ForeignKeyViolation\
                .treat(error=error, engine=engine)

        if TreatPsycopg2NotNullViolation.can_treat(error=error):
            return TreatPsycopg2NotNullViolation\
                .treat(error=error, engine=engine)

        if TreatPsycopg2CheckViolation.can_treat(error=error):
            return TreatPsycopg2CheckViolation\
                .treat(error=error, engine=engine)

        if TreatPsycopg2ExclusionViolation.can_treat(error=error):
            return TreatPsycopg2ExclusionViolation\
                .treat(error=error, engine=engine)

        if TreatPsycopg2RestrictViolation.can_treat(error=error):
            return TreatPsycopg2RestrictViolation\
                .treat(error=error, engine=engine)

        if TreatPsycopg2TriggeredActionException.can_treat(error=error):
            return TreatPsycopg2TriggeredActionException\
                .treat(error=error, engine=engine)

        else:
            message = (
                "Psycopg2Error error [{erro_type}] not treated. "
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
