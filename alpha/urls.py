"""alpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

apps_urls = [
    # For Admin Panel
    path("admin/", admin.site.urls),
]

api_apps_urls = [
    # For Products -API- App
    path("v1/products/", include("apps.products.api.urls", namespace="products_api")),
    # For Categories -API- APP
    path(
        "v1/categories/",
        include("apps.categories.api.urls", namespace="categories_api"),
    ),
    path("v1/cart/", include("apps.cart.api.urls"), name="cart_api"),
]

urlpatterns = apps_urls + api_apps_urls

# Setup Media URL On Dev Mood
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
