"""Auxiliary codes to treat expecific errors from sqlalchemy."""
from .unique_violation import TreatPsycopg2UniqueViolation
from .check_violation import TreatPsycopg2CheckViolation
from .exclusion_violation import TreatPsycopg2ExclusionViolation
from .foreignkey_violation import TreatPsycopg2ForeignKeyViolation
from .notnull_violation import TreatPsycopg2NotNullViolation
from .restrict_violation import TreatPsycopg2RestrictViolation
from .triggered_action_exception import TreatPsycopg2TriggeredActionException

__docformat__ = "google"

__all__ = [
    TreatPsycopg2UniqueViolation, TreatPsycopg2CheckViolation,
    TreatPsycopg2ExclusionViolation, TreatPsycopg2ForeignKeyViolation,
    TreatPsycopg2NotNullViolation, TreatPsycopg2RestrictViolation,
    TreatPsycopg2TriggeredActionException]
