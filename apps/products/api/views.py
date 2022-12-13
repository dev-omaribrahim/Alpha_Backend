from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from ..models import Product, ProductBag
from .serializers import ProductBagSerializer, ProductSerializer


class ProductBagListAPIView(APIView):
    """
    List All Produc Bags With/Without Category Filter
    """

    def get(self, request, category=None):

        products_bags = (
            ProductBag.objects.filter(category__name=category)
            if category
            else ProductBag.objects.all()
        )
        products_bags_serializer = ProductBagSerializer(products_bags, many=True)

        return Response(data=products_bags_serializer.data, status=status.HTTP_200_OK)


class ProductBagRetriveAPIView(APIView):
    """
    Retrive Product Bag And Display All Of It's Products
    """

    def get(self, request, pk):

        product_bag = get_object_or_404(ProductBag, pk=pk)
        products = product_bag.products

        product_bag_serializer = ProductBagSerializer(product_bag)
        products_serializer = ProductSerializer(products, many=True)

        data = {
            "Product_Bag": product_bag_serializer.data,
            "Products": products_serializer.data,
        }
        return Response(data=data, status=status.HTTP_200_OK)
