"""Class to treat unique violation raised from SQLAlchemy."""
import pandas as pd
from sqlalchemy.exc import IntegrityError
from sqlalchemy.engine import Engine


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


class TreatSQLAlchemyUniqueViolation:
    """Treat unique constrain error from database."""

    @classmethod
    def treat(cls, error: IntegrityError, engine: Engine) -> dict:
        """Treat SQLAlchemy Unique Violation.

        Args:
            error (IntegrityError):
                pass
            engine (Engine):
                pass
        Returns:
            Return a dictionary with message and other exception information.
        """
        query_results = pd.read_sql(
            query, con=engine, params={
                'table_name': error.orig.diag.table_name,
                'constraint_name': error.orig.diag.constraint_name})

        columns = query_results['column_name'].tolist()
        columns_str = ", ".join(columns)
        message = (
            "Unique constrain violated, columns [{columns_str}] must be "
            "unique.")
        return {
            "message": message,
            "type": "PumpWoodUniqueDatabaseError",
            "payload": {
                "db_error": str(error),
                "columns_str": columns_str,
                "columns": columns
            }
        }
