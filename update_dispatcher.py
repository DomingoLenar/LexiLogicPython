from abc import ABC, abstractmethod


class UpdateDispatcher(ABC):
    @abstractmethod
    def update(self, json_string):
        pass
