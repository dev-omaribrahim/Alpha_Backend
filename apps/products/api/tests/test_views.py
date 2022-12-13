from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from apps.categories.models import Category

from ...models import Product, ProductBag
from ..serializers import ProductBagSerializer, ProductSerializer

client = Client()


class ProductBagListAPIViewTest(TestCase):
    def setUp(self) -> None:
        """
        Setup Data To Be Used in Testing
        """
        self.image = SimpleUploadedFile(
            name="image.jpg", content=b"", content_type="image/jpeg"
        )

        self.category = Category.objects.create(name="Shoes")

        self.product_bags = [
            ProductBag(
                title="product_bag_test_1", image=self.image, category=self.category
            ),
            ProductBag(
                title="product_bag_test_2", image=self.image, category=self.category
            ),
            ProductBag(
                title="product_bag_test_3", image=self.image, category=self.category
            ),
        ]

        ProductBag.objects.bulk_create(self.product_bags)
        self.product_bags = ProductBag.objects.all()

    def test_get_all_products_bags(self):
        """
        Test The View Reutns The Expected Content And Status.
        Expected Results:
        => All Serialzed Product Bags
        => Status Cdoe 200_OK
        """
        response = client.get(reverse("products_api:product_bag_list"))
        serializer = ProductBagSerializer(self.product_bags, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products_bags_filtered_by_category(self):
        """
        Test The View Reutns The Expected Content And Status.
        Expected Results:
        => All Serialzed Product Bags Filtered By Category Name
        => Status Cdoe 200_OK
        """
        category = Category.objects.first()
        response = client.get(
            reverse(
                "products_api:product_bag_list_filter",
                kwargs={"category": category.name},
            )
        )
        filtered_product_bags = self.product_bags.filter(category__name=category.name)
        serializer = ProductBagSerializer(filtered_product_bags, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProductBagRetriveAPIViewTest(TestCase):
    def setUp(self):
        """
        Setup Data To Be Used At Testing
        """
        self.image = SimpleUploadedFile(
            name="image.jpg", content=b"", content_type="image/jpeg"
        )

        self.category = Category.objects.create(name="Shoes")

        self.product_bag = ProductBag.objects.create(
            title="product_bag_test_1", image=self.image, category=self.category
        )

        products = [
            Product(
                name="Test1",
                price=10,
                image=self.image,
                code="1",
                description="test",
                renewable=False,
                session_url="",
                product_bag=self.product_bag,
            ),
            Product(
                name="Test2",
                price=10,
                image=self.image,
                code="1",
                description="test",
                renewable=False,
                session_url="",
                product_bag=self.product_bag,
            ),
            Product(
                name="Test3",
                price=10,
                image=self.image,
                code="1",
                description="test",
                renewable=False,
                session_url="",
                product_bag=self.product_bag,
            ),
        ]

        Product.objects.bulk_create(products)

    def test_retrive_valid_product_bag(self):
        """
        Test The View Reutns The Expected Content And Status.
        Expected Results:
        => Retrive A Single Product Bag And All Of It's Products
        => Status Cdoe 200_OK
        """
        response = client.get(
            reverse(
                "products_api:product_bag_detail", kwargs={"pk": self.product_bag.pk}
            )
        )

        product_bag_serializer = ProductBagSerializer(self.product_bag)
        products_serializer = ProductSerializer(self.product_bag.products, many=True)

        data = {
            "Product_Bag": product_bag_serializer.data,
            "Products": products_serializer.data,
        }

        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrive_invalid_product_bag(self):
        """
        Test The View Reutns The Expected Status.
        Expected Stauts:
        => Try To Retrive Not Existend Product Bag
        => Status Cdoe 404_NOT_FOUND
        """
        response = client.get(
            reverse("products_api:product_bag_detail", kwargs={"pk": 3000})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
