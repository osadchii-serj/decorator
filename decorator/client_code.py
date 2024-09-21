from love_republic_products import LoveRepublicTweedPencilSkirt
from love_republic_products import LoveRepublicPalazzoTrousers
from love_republic_products import LoveRepublicDenimJumpsuit
from love_republic_products import LoveRepublicTweedJacket
from love_republic_products import LoveRepublicShorts

from discount_decorator import DiscountDecorator

from love_republic import LoveRepublic

from interfaces.discount import Discount
from interfaces.product import Product
from interfaces.shop import Shop

from random import choice


def client_code(shop: Shop, product: Product, discount: Discount):
    print("===" * 30)
    shop = shop(discount(product()))
    disc, currency = shop.get_product()
    print(f"Цена со скидкой {round(disc)} {currency} :)")
    print()
    print("===" * 30)


if __name__ == "__main__":

    products = [
        LoveRepublicTweedPencilSkirt,
        LoveRepublicPalazzoTrousers,
        LoveRepublicDenimJumpsuit,
        LoveRepublicTweedJacket,
        LoveRepublicShorts,
    ]

    for _ in range(10):
        product = choice(products)
        client_code(LoveRepublic, product, DiscountDecorator)
