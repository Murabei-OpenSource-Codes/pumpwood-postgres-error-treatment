"""Auxiliary codes to treat expecific errors from sqlalchemy."""
from .general import TreatPsycopg2Error


__all__ = [
    TreatPsycopg2Error
]


__docformat__ = "google"
