"""Auxiliary functions to extract information from psycopg2 errors."""
from sqlalchemy.exc import IntegrityError


def extract_pg_diagnostics(error: IntegrityError) -> dict:
    """Extract psycopg2 diagnostics.

    Args:
        error (IntegrityError):
            Error that will be treated and extracted information.

    Returns:
        Returns a dictionary with keys:
            - schema: Schema associated with error.
            - table: Table associated with error.
            - column: Column associated with error.
            - constraint: Constraint associated with error.
            - message: Message associated with error.
            - detail: Detail associated with error.
            - hint: Hint associated with error.
    """
    diag = getattr(error, "diag", None)
    if not diag:
        return {}
    return {
        "schema": getattr(diag, "schema_name", None),
        "table": getattr(diag, "table_name", None),
        "column": getattr(diag, "column_name", None),
        "constraint": getattr(diag, "constraint_name", None),
        "message": getattr(diag, "message_primary", None),
        "hint": getattr(diag, "message_hint", None),
    }
