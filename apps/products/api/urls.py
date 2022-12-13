from django.urls import path

from . import views

app_name = "products_api"


urlpatterns = [
    # For Product Bag List API View
    path(
        "product-bags/", views.ProductBagListAPIView.as_view(), name="product_bag_list"
    ),
    path(
        "product-bags/category/<str:category>/",
        views.ProductBagListAPIView.as_view(),
        name="product_bag_list_filter",
    ),
    # For Product Bag Retrive API View
    path(
        "product-bags/<int:pk>/",
        views.ProductBagRetriveAPIView.as_view(),
        name="product_bag_detail",
    ),
]
