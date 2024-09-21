from abc import ABC, abstractmethod


class Shop(ABC):

    @abstractmethod
    def get_product(self):
        pass
