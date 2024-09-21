from abc import ABC, abstractmethod


class Discount(ABC):

    @abstractmethod
    def get_instance(self):
        pass
