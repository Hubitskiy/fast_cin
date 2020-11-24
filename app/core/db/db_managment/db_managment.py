from attr import attrs

from core.db.utils import DBConnection


@attrs(auto_attribs=True)
class DB:
    db_connect: DBConnection
