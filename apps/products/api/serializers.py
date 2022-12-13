from rest_framework import serializers

from apps.categories.api.serializers import CategorySerializer

from ..models import Product, ProductBag, ProductStock


class ProductStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStock
        fields = ["color", "size", "quantity"]


class ProductSerializer(serializers.ModelSerializer):
    stocks = ProductStockSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "image",
            "code",
            "description",
            "renewable",
            "session_url",
            "stocks",
        ]


class ProductBagSerializer(serializers.ModelSerializer):
    # Not Sure if i need category for now.
    # category = CategorySerializer()

    class Meta:
        model = ProductBag
        fields = [
            "title",
            "image",
            #  "category"
        ]
