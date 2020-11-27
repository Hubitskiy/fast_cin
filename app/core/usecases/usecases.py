from abc import abstractmethod


class BaseUseCase:

    def validate(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):

        self.validate(*args, **kwargs)

        return self.execute(*args, **kwargs)


class BaseService:
    pass
