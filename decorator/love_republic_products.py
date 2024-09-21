from interfaces.product import Product
from dataclasses import dataclass


@dataclass
class LoveRepublicTweedJacket(Product):
    _name = "Твидовый жакет"
    _currency = "RUB"
    _price = 10999

    def get_instance(self):
        print(self.__class__)
        print(f"Название товара: {self._name}")
        print(f"Цена: {self._price} {self._currency}")
        return self._name, self._price, self._currency


@dataclass
class LoveRepublicShorts(Product):
    _name = "Шорты"
    _currency = "RUB"
    _price = 3999

    def get_instance(self):
        print(self.__class__)
        print(f"Название товара: {self._name}")
        print(f"Цена: {self._price} {self._currency}")
        return self._name, self._price, self._currency


@dataclass
class LoveRepublicPalazzoTrousers(Product):
    _name = "Брюки-палаццо"
    _currency = "RUB"
    _price = 4999

    def get_instance(self):
        print(self.__class__)
        print(f"Название товара: {self._name}")
        print(f"Цена: {self._price} {self._currency}")
        return self._name, self._price, self._currency


@dataclass
class LoveRepublicDenimJumpsuit(Product):
    _name = "Джинсовый комбинезон"
    _currency = "RUB"
    _price = 11999

    def get_instance(self):
        print(self.__class__)
        print(f"Название товара: {self._name}")
        print(f"Цена: {self._price} {self._currency}")
        return self._name, self._price, self._currency


@dataclass
class LoveRepublicTweedPencilSkirt(Product):
    _name = "Твидовая юбка-карандаш"
    _currency = "RUB"
    _price = 5599

    def get_instance(self):
        print(self.__class__)
        print(f"Название товара: {self._name}")
        print(f"Цена: {self._price} {self._currency}")
        return self._name, self._price, self._currency
