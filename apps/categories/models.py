from django.db import models


class Category(models.Model):
    """
    Categories For Products
    """

    name = models.CharField(
        max_length=100, null=False, blank=False, default="unnamed category", unique=True
    )

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.name


# place_holder_category, created = Category.objects.get_or_create(name="place_holder_category")

# PLACE_HOLDER_CATEGORY_ID = place_holder_category.id
# PLACE_HOLDER_CATEGORY_NAME = place_holder_category.name
