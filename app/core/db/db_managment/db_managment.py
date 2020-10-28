class BaseCRUDDBManagement(type):

    allowed_methods = ("create", "retrieve", "update", "delete")

    def __new__(cls, name, attributes, dct):
        child_class = super().__new__(cls, name, attributes, dct)

        class_attrs = child_class.__dict__

        if not any(attr in cls.allowed_methods for attr in class_attrs):
            raise NotImplementedError(
                f"You must implement at least one of the following methods: {cls.allowed_methods}"
            )

        return child_class
