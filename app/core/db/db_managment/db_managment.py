from core.db.utils import DBConnectionManager


__all__ = ["BaseCRUDDBManagement"]


class BaseCRUDDBManagement(type):

    a_m = ["create", "retrieve", "update", "delete"]

    def __new__(mcs, name, bases, dct):

        if not any(
                meth.startswith(m)
                for meth in dct
                for m in mcs.a_m
        ):
            raise NotImplementedError(
                f"You must implement at least one of the following methods: {mcs.a_m}"
            )

        return type.__new__(mcs, name, bases, dct)

    def __init__(cls, name, attributes, dct):

        cls.db = DBConnectionManager()

        super().__init__(name, attributes, dct)
