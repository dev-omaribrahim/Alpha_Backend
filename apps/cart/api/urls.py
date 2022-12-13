from django.urls import path

from . import views

app_name = "cart_api"

urlpatterns = [
    path("", views.CartListCreateAPIView.as_view(), name="cart_list_create"),
    path(
        "single/", views.CartUpdateDeletelAPIView.as_view(), name="cart_update_delete"
    ),
    path("clear/", views.CartClearAPIView.as_view(), name="cart_clear"),
]
