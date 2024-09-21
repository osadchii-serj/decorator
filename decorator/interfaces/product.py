from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Product(ABC):
    _name = None
    _price = 0.0
    _currency = None

    @abstractmethod
    def get_instance(self):
        pass
