from django.core.validators import MinValueValidator
from django.db import models

from apps.categories.models import Category

# , PLACE_HOLDER_CATEGORY_ID, PLACE_HOLDER_CATEGORY_NAME


def product_image_path(instance, filename):
    """
    Dynamic Path For Saving Images
    """
    return "image/"


class AbstractProductModel(models.Model):
    """
    Base Class For Product Model shared info,
    That Will be Used In More Than One Model.
    """

    name = models.CharField(
        max_length=255, null=False, blank=False, default="Unnamed Product"
    )

    price = models.PositiveIntegerField(
        null=False, blank=False, default=0, validators=[MinValueValidator(0)]
    )

    image = models.ImageField(upload_to=product_image_path, default="default.jfif")

    code = models.CharField(max_length=255, null=False, blank=True, default="")

    description = models.TextField(null=True, blank=True, default="")

    class Meta:
        abstract = True

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.name


class ProductBag(models.Model):
    """
    The Bag That Contains More Than Product Of The Same Type,
    For EX: Many Colors For The Same T-Shirt
    """

    title = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to=product_image_path, default="default.jfif")
    category = models.ForeignKey(
        Category,
        null=False,
        blank=False,
        related_name="product_bags",
        on_delete=models.CASCADE,
        default="",
    )

    def __str__(self) -> str:
        return self.title


class Product(AbstractProductModel):
    """
    The Actual Model That Will Be Displayed For Clients.
    """

    renewable = models.BooleanField(null=True, blank=True, default=False)
    session_url = models.URLField(
        max_length=255,
        null=True,
        blank=True,
    )

    product_bag = models.ForeignKey(
        ProductBag,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="products",
        default="",
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductStock(models.Model):
    """
    The Size/Color and Its Amount Or Just The Amount If No Size/Color.
    """

    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        related_name="stocks",
        on_delete=models.CASCADE,
    )
    color = models.CharField(max_length=50, null=True, blank=True, default="")
    size = models.CharField(max_length=50, null=True, blank=True, default="")
    quantity = models.PositiveIntegerField(
        null=False, blank=False, default="0", validators=[MinValueValidator(0)]
    )

    def get_absolute_url(self):
        pass

    def __str__(self):
        return f"{self.product.name}-{self.size}-{self.quantity}"
