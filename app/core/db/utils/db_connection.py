from fastapi import Depends

from core.db.database import SessionLocal


class DBConnectionManager:

    def __init__(self, db: SessionLocal = Depends(SessionLocal)):
        self.db = db

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()
