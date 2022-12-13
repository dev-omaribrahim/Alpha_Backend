from typing import Generator

from django.conf import settings


class Cart:
    """
    Cart class is for:
    - managing all CRUD operations on the cart.
    - perform money operations (total prices, total commissions, total cart Price).
    - ease iteration over products.
    - get total count of products number.
    """

    def __init__(self, request):
        """
        Get the session and initialise The cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID, None)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_data: dict) -> None:
        """
        - Add product to the cart session if Not in the cart.
        - Increment it's quantity in the cart if the product already in the cart.
        """
        # Craft unique id for the products in the cart
        product_crafted_id = (
            product_data.get("product_id", "")
            + product_data.get("color", "")
            + product_data.get("size", "")
        )
        if product_crafted_id not in self.cart.keys():
            self.cart[product_crafted_id] = {
                "product_crafted_id": product_crafted_id,
                "product_id": product_data.get("product_id", ""),
                "price": product_data.get("price", ""),
                "quantity": product_data.get("quantity", ""),
                "color": product_data.get("color", ""),
                "size": product_data.get("size", ""),
                "commission": product_data.get("commission", ""),
            }

            self.save()

    def update(self, product_data: dict) -> None:
        """
        Update the quantity and commission in the cart
        """
        product_crafted_id = product_data.get("product_crafted_id", "")
        if product_crafted_id in self.cart.keys():
            self.cart[product_crafted_id]["quantity"] = product_data.get("quantity", "")
            self.cart[product_crafted_id]["commission"] = product_data.get(
                "commission", ""
            )
            self.save()

    def remove(self, product_data: dict) -> None:
        """
        Remove the product from the cart
        """
        product_crafted_id = product_data.get("product_crafted_id", "")
        if product_crafted_id in self.cart.keys():
            del self.cart[product_crafted_id]
            # No need to be Expilict save here,
            # But Make it expilict to be sure just in case
            self.save()

    def clear(self) -> None:
        """
        Remove all products from the cart
        """
        if self.cart:
            del self.session[settings.CART_SESSION_ID]
            # No need to be Expilict save here,
            # But Make it expilict to be sure just in case
            self.save()

    def save(self) -> None:
        """
        Mark session as modiefied for further reading:
        https://docs.djangoproject.com/en/3.2/topics/http/sessions/#when-sessions-are-saved
        """
        self.session.modified = True

    def __iter__(self) -> Generator:
        """
        Retrun a generator that return product stored in dict each iteration,
        Make it easy to loop over products
        """
        for product in self.cart.values():
            yield product

    def __len__(self) -> int:
        """
        Return the total piecies number of products putted in the cart
        """
        quantities = [int(product["quantity"]) for product in self.cart.values()]
        return sum(quantities)

    def get_total_products_price(self) -> int:
        """
        Calculate the price of all products in the cart
        """
        prices = [
            int(product["price"]) * int(product["quantity"])
            for product in self.cart.values()
        ]
        return sum(prices)

    def get_total_commissions(self) -> int:
        """
        Calculate the commission of all products in the cart
        """
        commissions = [
            int(product["commission"]) * int(product["quantity"])
            for product in self.cart.values()
        ]
        return sum(commissions)

    def get_total_cart_price(self) -> int:
        """
        Calculate the total final price of the cart
        """
        return self.get_total_products_price() + self.get_total_commissions()
