from core.db.database import Database


class DBConnectionManager:

    def __init__(self):
        self.db = Database

    def __enter__(self):
        return self.db.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.session.close()
