from abc import ABC, abstractmethod


__all__ = ["BasePresenter", "RetrievePresenter", "CreatePresenter", "UpdatePresenter", "DeletePresenter"]


class BasePresenter(ABC):
    pass


class RetrievePresenter(BasePresenter):

    @abstractmethod
    def retrieve(self, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self.retrieve()


class CreatePresenter(BasePresenter):

    @abstractmethod
    def create(self, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self.create()


class UpdatePresenter(BasePresenter):

    @abstractmethod
    def update(self, partial: bool = False, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self.update()


class DeletePresenter(BasePresenter):

    @abstractmethod
    def delete(self, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self.delete()
