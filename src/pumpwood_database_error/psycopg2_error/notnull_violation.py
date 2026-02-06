"""Class to treat unique violation raised from SQLAlchemy."""
from sqlalchemy.engine import Engine
from psycopg2.errors import NotNullViolation
from pumpwood_communication.exceptions import PumpWoodDatabaseError
from pumpwood_database_error.abc import ErrorTreatmentABC

from .auxiliary import extract_pg_diagnostics


class TreatPsycopg2NotNullViolation(ErrorTreatmentABC):
    """Treat unique constrain error from database."""

    @classmethod
    def can_treat(cls, error: Exception) -> bool:
        """Check if error is of the type treated by this class.

        Returns:
            Returns true if error is of the class treated by this class.
        """
        return isinstance(error, NotNullViolation)

    @classmethod
    def treat(cls, error: NotNullViolation, engine: Engine) -> dict:
        """Treat psycopg2 error.

        Args:
            error (NotNullViolation):
                Psycopg2 NotNullViolation error.
            engine (Engine):
                SQLAlchemy engine, it is used to get information from
                database and log error.

        Returns:
            Return a dictionary with message and other exception information.
        """
        pg_diag = extract_pg_diagnostics(error)
        message = (
            "Null Violation Database error, column [{column}] must not "
            "be null. Database message:\n{message}")
        return PumpWoodDatabaseError(message=message, payload=pg_diag)\
            .to_dict()
