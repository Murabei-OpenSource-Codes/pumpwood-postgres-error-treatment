"""Class to treat unique violation raised from SQLAlchemy."""
from sqlalchemy.engine import Engine
from psycopg2.errors import TriggeredActionException
from pumpwood_communication.exceptions import PumpWoodDatabaseError
from .auxiliary import extract_pg_diagnostics


class TreatPsycopg2TriggeredActionException:
    """Treat unique constrain error from database."""

    @classmethod
    def treat(cls, error: TriggeredActionException, engine: Engine) -> dict:
        """Treat psycopg2 error.

        Args:
            error (TriggeredActionException):
                Psycopg2 TriggeredActionException error.
            engine (Engine):
                SQLAlchemy engine, it is used to get information from
                database and log error.

        Returns:
            Return a dictionary with message and other exception information.
        """
        pg_diag = extract_pg_diagnostics(error)
        message = "Restrict Violation Database error:\n{message}"
        return PumpWoodDatabaseError(message=message, payload=pg_diag)\
            .to_dict()
