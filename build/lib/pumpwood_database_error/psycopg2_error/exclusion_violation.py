"""Class to treat unique violation raised from SQLAlchemy."""
from sqlalchemy.engine import Engine
from psycopg2.errors import ExclusionViolation
from pumpwood_communication.exceptions import PumpWoodDatabaseError
from pumpwood_database_error.abc import ErrorTreatmentABC

from .auxiliary import extract_pg_diagnostics


class TreatPsycopg2ExclusionViolation(ErrorTreatmentABC):
    """Treat unique constrain error from database."""

    @classmethod
    def can_treat(cls, error: Exception) -> bool:
        """Check if error is of the type treated by this class.

        Returns:
            Returns true if error is of the class treated by this class.
        """
        return isinstance(error, ExclusionViolation)

    @classmethod
    def treat(cls, error: ExclusionViolation, engine: Engine) -> dict:
        """Treat psycopg2 error.

        Args:
            error (ExclusionViolation):
                Psycopg2 ExclusionViolation error.
            engine (Engine):
                SQLAlchemy engine, it is used to get information from
                database and log error.

        Returns:
            Return a dictionary with message and other exception information.
        """
        pg_diag = extract_pg_diagnostics(error)
        message = "Exclusion Violation Database error:\n{message}"
        return PumpWoodDatabaseError(message=message, payload=pg_diag)\
            .to_dict()
