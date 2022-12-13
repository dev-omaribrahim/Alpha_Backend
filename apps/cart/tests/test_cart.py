from django.test import Client, TestCase

from ..cart import Cart


class CartCRUDTestCase(TestCase):
    """
    This Tesct Case for testing:
    - cart add method
    - cart update method
    - cart remove method
    """

    @classmethod
    def setUpTestData(cls):
        cls.valid_product_payload = {
            "product_crafted_id": "3blue2xl",
            "product_id": "3",
            "price": "20",
            "quantity": "4",
            "color": "blue",
            "size": "2xl",
            "commission": "5",
        }

        cls.valid_update_product_payload = {
            "product_crafted_id": "3blue2xl",
            "product_id": "3",
            "price": "20",
            "quantity": "1",
            "color": "blue",
            "size": "2xl",
            "commission": "54",
        }

    def setUp(self):
        self.client = Client()
        self.cart = Cart(self.client)

    def get_cart_items(self):
        products = [product for product in self.cart]
        return products

    def test_add_method(self):
        self.cart.add(self.valid_product_payload)
        self.assertCountEqual([self.valid_product_payload], self.get_cart_items())

    def test_update_method(self):
        self.cart.add(self.valid_product_payload)
        self.cart.update(self.valid_update_product_payload)
        self.assertCountEqual(
            [self.valid_update_product_payload], self.get_cart_items()
        )

    def test_remove_method(self):
        self.cart.add(self.valid_product_payload)
        self.cart.remove(self.valid_product_payload)
        self.assertCountEqual([], self.get_cart_items())
