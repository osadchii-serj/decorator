from interfaces.product import Product
from interfaces.shop import Shop
from dataclasses import dataclass


@dataclass
class LoveRepublic(Shop):
    _product: Product

    _description = (
        "MELON FASHION GROUP — крупнейший и быстрорастущий fashion-ритейл России"
    )
    _name = "Love Republic"

    def get_product(self):
        self.show_description()
        return self._product.get_instance()

    def show_description(self):
        print()
        print(self.__class__)
        print(self._name)
        print(self._description)
        print()
