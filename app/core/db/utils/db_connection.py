from core.db.database import Database
from attr import attrs


@attrs(auto_attribs=True)
class DBConnection:
    db: Database

    def __enter__(self):
        return self.db.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.session.close()
