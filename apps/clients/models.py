from django.db import models


class Client(models.Model):
    name = models.CharField(
        max_length=100, null=False, blank=False, default="default name"
    )
    address = models.CharField(
        max_length=250, null=False, blank=False, default="default address"
    )
    mobile_number_1 = models.CharField(
        max_length=11, null=False, blank=False, default="default name"
    )
    mobile_number_2 = models.CharField(
        max_length=11, null=False, blank=False, default="default name"
    )

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self) -> str:
        return self.name
