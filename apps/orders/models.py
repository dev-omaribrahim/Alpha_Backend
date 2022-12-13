from django.db import models

from apps.products.models import AbstractProductModel
from apps.users.models import Marketer


def product_image_path(instance, filename):
    """
    Dynamic Path For Saving Images
    """
    return "image/"


class Order(models.Model):
    notes = models.TextField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    marketer = models.ForeignKey(
        Marketer,
        null=False,
        blank=False,
        related_name="orders",
        on_delete=models.CASCADE,
    )


class OrderProduct(AbstractProductModel):
    image = models.ImageField(
        upload_to=product_image_path, null=True, blank=True, default="default.jfif"
    )
    order_info = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        related_name="products",
        on_delete=models.CASCADE,
    )
