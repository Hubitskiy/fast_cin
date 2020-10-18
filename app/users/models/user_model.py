from core.db.database import Base

from sqlalchemy import Integer, String, Boolean, Column


class UserModel(Base):

    __tablename__ = "users"

    id = Column(
        Integer, primary_key=True, autoincrement=True, index=True)

    email = Column(
        String, index=True, unique=True, nullable=False)

    hashed_password = Column(
        String, nullable=False)

    first_name = Column(
        String, nullable=False)

    last_name = Column(
        String, nullable=False, index=True)

    is_active = Column(
        Boolean, default=False)

    is_admin = Column(
        Boolean, default=False)
