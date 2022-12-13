from rest_framework.views import APIView, Response, status

from ..cart import Cart
from ..utiles import build_cart_methods_context
from .serializer import CartSerializer


class CartListCreateAPIView(APIView):
    """
    - get: get all products in the cart.
    - post: add product to the cart, (data shape in the docs).
    - delete: remove all products in the cart
    """

    def get(self, request):
        cart = Cart(request)
        products = [product for product in cart]
        cart_serializer = CartSerializer(
            products, many=True, cart=cart, request=request
        )
        return Response(data=cart_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        cart = Cart(request)
        cart_serializer = CartSerializer(data=request.data, cart=cart, request=request)
        if cart_serializer.is_valid():
            cart_serializer.add_product()
            return Response(data=cart_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartUpdateDeletelAPIView(APIView):
    """
    - patch: update (single) product (commission and quantity), (data shape in the docs).
    - delete: remove (single) product, (data shape in the docs).
    """

    def patch(self, request):
        cart = Cart(request)
        cart_serializer = CartSerializer(data=request.data, cart=cart, request=request)
        if cart_serializer.is_valid():
            cart_serializer.update_product()
            return Response(data=cart_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        cart = Cart(request)
        cart_serializer = CartSerializer(data=request.data, cart=cart, request=request)
        if cart_serializer.is_valid():
            cart_serializer.remove_product()
            return Response(data=cart_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartClearAPIView(APIView):
    """
    - delete: remove all products in the cart at once.
    """

    def delete(self, request):
        cart = Cart(request)
        cart.clear()
        return Response(status=status.HTTP_204_NO_CONTENT)
