"""ocrnightmare Admin API Rollback Route Controller"""
from flask import Blueprint

rollback = Blueprint(
        "rollback", __name__,
    )

from .rollback import rollback # type: ignore[misc]  # pylint: disable=wrong-import-position


