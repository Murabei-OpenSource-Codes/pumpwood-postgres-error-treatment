"""Errors associated with object not found using SQLAlchemy."""
from sqlalchemy.exc import NoResultFound
from sqlalchemy.engine import Engine
from pumpwood_communication.exceptions import PumpWoodObjectDoesNotExist
from pumpwood_database_error.abc import ErrorTreatmentABC


class TreatSQLAlchemyNoResultFound(ErrorTreatmentABC):
    """Treat unique constrain error from database."""

    @classmethod
    def can_treat(cls, error: Exception) -> bool:
        """Check if error is of the type treated by this class.

        Returns:
            Returns true if error is of the class treated by this class.
        """
        return isinstance(error, NoResultFound)

    @classmethod
    def treat(cls, error: NoResultFound, engine: Engine) -> dict:
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
        message = "Object not found"
        return PumpWoodObjectDoesNotExist(message=message, payload={})\
            .to_dict()
