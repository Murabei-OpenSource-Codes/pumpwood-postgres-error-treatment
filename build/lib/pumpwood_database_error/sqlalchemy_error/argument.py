"""Errors associated with SQLAlchemy query arguments."""
from sqlalchemy.exc import ArgumentError
from sqlalchemy.engine import Engine
from pumpwood_communication.exceptions import PumpWoodQueryException
from pumpwood_database_error.abc import ErrorTreatmentABC


class TreatSQLAlchemyArgumentError(ErrorTreatmentABC):
    """Treat query argument error."""

    @classmethod
    def can_treat(cls, error: Exception) -> bool:
        """Check if error is of the type treated by this class.

        Returns:
            Returns true if error is of the class treated by this class.
        """
        return isinstance(error, ArgumentError)

    @classmethod
    def treat(cls, error: ArgumentError, engine: Engine) -> dict:
        """Treat sqlalchemy not found errors.

        Args:
            error (NoResultFound):
                Psycopg2 CheckViolation error.
            engine (Engine):
                SQLAlchemy engine, it is used to get information from
                database and log error.

        Returns:
            Return a dictionary with message and other exception information.
        """
        message = (
            "Error when building the query, check implementation.")
        return PumpWoodQueryException(
            message=message, payload={"error_message": str(error)})\
            .to_dict()
