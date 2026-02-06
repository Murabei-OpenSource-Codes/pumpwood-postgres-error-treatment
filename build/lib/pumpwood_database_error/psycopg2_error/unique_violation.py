"""Class to treat unique violation raised from SQLAlchemy."""
import pandas as pd
from sqlalchemy.engine import Engine
from psycopg2.errors import UniqueViolation
from pumpwood_communication.exceptions import PumpWoodUniqueDatabaseError
from pumpwood_database_error.abc import ErrorTreatmentABC

from .auxiliary import extract_pg_diagnostics


query = """
SELECT
    kcu.constraint_name,
    kcu.table_name,
    kcu.column_name
FROM
    information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
  ON tc.constraint_name = kcu.constraint_name
WHERE 1=1
  AND tc.constraint_type='UNIQUE'
  AND kcu.table_name=%(table_name)s
  AND kcu.constraint_name=%(constraint_name)s
"""


class TreatPsycopg2UniqueViolation(ErrorTreatmentABC):
    """Treat unique constrain error from database."""

    @classmethod
    def can_treat(cls, error: Exception) -> bool:
        """Check if error is of the type treated by this class.

        Returns:
            Returns true if error is of the class treated by this class.
        """
        return isinstance(error, UniqueViolation)

    @classmethod
    def treat(cls, error: UniqueViolation, engine: Engine) -> dict:
        """Treat psycopg2 error.

        Args:
            error (UniqueViolation):
                Psycopg2 UniqueViolation error.
            engine (Engine):
                SQLAlchemy engine, it is used to get information from
                database and log error.

        Returns:
            Return a dictionary with message and other exception information.
        """
        pg_diag = extract_pg_diagnostics(error)

        # Extract columns associated with columns
        query_results = pd.read_sql(
            query, con=engine, params={
                'table_name': pg_diag['table'],
                'constraint_name': pg_diag['constraint']})
        columns = query_results['column_name'].tolist()
        unique_columns = ", ".join(columns)
        message = (
            "Unique constrain violated, columns {columns} must be "
            "unique.")
        pg_diag['unique_columns'] = unique_columns
        pg_diag['columns'] = columns
        return PumpWoodUniqueDatabaseError(message=message, payload=pg_diag)\
            .to_dict()
