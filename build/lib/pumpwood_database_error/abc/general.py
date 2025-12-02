"""Define Abstract Base Classes for error treatment."""
from abc import ABC, abstractmethod
from sqlalchemy.engine import Engine


class ErrorTreatmentABC(ABC):
    """Class to define base implementation for error treatment."""

    @classmethod
    @abstractmethod
    def can_treat(cls, error: Exception) -> bool:
        """Check if error is of the type treated by this class.

        Returns:
            Returns true if error is of the class treated by this class.
        """
        pass

    @classmethod
    @abstractmethod
    def treat(cls, error: Exception, engine: Engine) -> dict:
        """Treat error an return a dictionary.

        Args:
            error (NoResultFound):
                Psycopg2 CheckViolation error.
            engine (Engine):
                SQLAlchemy engine, it is used to get information from
                database and log error.

        Returns:
            Return a dictionary with message and other exception information.
        """
        pass
