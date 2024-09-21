from interfaces.discount import Discount
from interfaces.product import Product
from dataclasses import dataclass
from random import randrange


@dataclass
class DiscountDecorator(Discount):
    _product: Product

    def get_instance(self):
        discount = randrange(0, 100, 5)
        _, price, currency = self._product.get_instance()
        print()
        print(self.__class__)
        print(f"Discount: {discount}%")
        return price - (discount / 100) * price, currency
