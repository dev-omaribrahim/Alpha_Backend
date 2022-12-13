import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from ...cart import Cart
from ..serializer import CartSerializer


class CartListCreateAPIViewTest(TestCase):
    """
    This Test Case is for:
    - Test view response status code.
    - Test the validation of the serializer.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.cart = Cart(cls.client)

    @classmethod
    def setUpTestData(cls):
        cls.valid_product_payload = {
            "product_id": "3",
            "price": "20",
            "quantity": "4",
            "color": "blue",
            "size": "2xl",
            "commission": "5",
        }
        cls.invalid_product_payload = {
            "product_id": "",
            "price": "",
            "quantity": "",
            "color": "",
            "size": "",
            "commission": "",
        }

    def test_valid_payload_cart_add_method(self):
        response = self.client.post(
            reverse("cart_api:cart_list_create"),
            data=json.dumps(self.valid_product_payload),
            content_type="application/json",
        )
        serializer = CartSerializer(data=self.valid_product_payload)
        self.assertEqual(serializer.is_valid(), True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_payload_cart_add_method(self):
        response = self.client.post(
            reverse("cart_api:cart_list_create"),
            data=json.dumps(self.invalid_product_payload),
            content_type="application/json",
        )
        serializer = CartSerializer(data=self.invalid_product_payload)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_producs(self):
        response = self.client.get(reverse("cart_api:cart_list_create"))
        # products = [product for product in self.cart]
        # serializer = CartSerializer(products, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CartUpdateDeletelAPIViewTest(TestCase):
    """
    This Test Case is for:
    - Test view response status code.
    - Test the validation of the serializer.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.cart = Cart(cls.client)

    @classmethod
    def setUpTestData(cls):
        cls.valid_product_payload = {
            "product_id": "3",
            "price": "20",
            "quantity": "4",
            "color": "blue",
            "size": "2xl",
            "commission": "5",
        }
        cls.valid_product_update_payload = {
            "product_crafted_id": "3blue2xl",
            "product_id": "3",
            "price": "20",
            "quantity": "1",
            "color": "blue",
            "size": "2xl",
            "commission": "70",
        }
        cls.invalid_product_payload = {
            "product_id": "",
            "price": "",
            "quantity": "",
            "color": "",
            "size": "",
            "commission": "",
        }

    def test_valid_payload_cart_update_method(self):
        self.cart.add(self.valid_product_payload)
        response = self.client.patch(
            reverse("cart_api:cart_update_delete"),
            data=json.dumps(self.valid_product_update_payload),
            content_type="application/json",
        )
        serializer = CartSerializer(data=self.valid_product_update_payload)
        self.assertEqual(serializer.is_valid(), True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_payload_cart_update_method(self):
        response = self.client.patch(
            reverse("cart_api:cart_update_delete"),
            data=json.dumps(self.invalid_product_payload),
            content_type="application/json",
        )
        serializer = CartSerializer(data=self.invalid_product_payload)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_payload_cart_delete_method(self):
        response = self.client.delete(
            reverse("cart_api:cart_update_delete"),
            data=json.dumps(self.valid_product_payload),
            content_type="application/json",
        )
        serializer = CartSerializer(data=self.valid_product_update_payload)
        self.assertEqual(serializer.is_valid(), True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_payload_cart_delete_method(self):
        response = self.client.delete(
            reverse("cart_api:cart_update_delete"),
            data=json.dumps(self.invalid_product_payload),
            content_type="application/json",
        )
        serializer = CartSerializer(data=self.invalid_product_payload)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CartUpdateDeletelAPIViewTest(TestCase):
    """
    This Test Case is for:
    - Test view response status code.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def test_valid_payload_cart_delete_method(self):
        response = self.client.delete(reverse("cart_api:cart_clear"))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
