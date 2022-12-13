from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from apps.categories.models import Category

from ...models import Product, ProductBag, ProductStock
from ..serializers import (ProductBagSerializer, ProductSerializer,
                           ProductStockSerializer)


class ProductBagSerializerTest(TestCase):
    def setUp(self) -> None:
        """
        Setup Data To Be Used in Testing
        """
        self.image = SimpleUploadedFile(
            name="image.jpg", content=b"", content_type="image/jpeg"
        )

        self.category = Category.objects.create(name="shirts")

        self.valid_product_bag = {
            "title": "test",
            "image": self.image,
            "category": self.category,
        }

        self.product_bag = ProductBag.objects.create(**self.valid_product_bag)

        self.serializer_fields = ["title", "image"]

        self.serializer_data = ProductBagSerializer(instance=self.product_bag).data

    def test_contains_expected_fields(self):
        """
        This Test To guarantee that the addition or removal of any field to the serializer
        will be noticed by the tests.
        """
        data = self.serializer_data
        # Check if The Two Lists Have The Same Elements Regardless of thier Order
        self.assertCountEqual(list(data.keys()), self.serializer_fields)

    def test_fields_valid_values(self):
        """
        This Test To Check That Serializer Returns The Expected Values
        """
        data = self.serializer_data
        self.assertEqual(data["title"], self.valid_product_bag["title"])
        self.assertEqual(data["image"], self.product_bag.image.url)
