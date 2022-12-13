from django.contrib import admin

from .models import Product, ProductBag, ProductStock


class StockInline(admin.TabularInline):
    model = ProductStock
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [StockInline]


admin.site.register(ProductBag)
admin.site.register(ProductStock)
