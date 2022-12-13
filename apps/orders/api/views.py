from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from apps.orders.models import Order

from .serializers import OrderSerializer


class OrderListCreateAPIView(APIView):
    def get(self, request):
        orders = Order.objects.filter(marketer=request.user.pk)
        serializer = OrderSerializer(orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailAPIView(APIView):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
