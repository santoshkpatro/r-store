
from django.contrib import admin
from django.urls import path, include

from . views import index, about, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/", about),
    path("contact/", contact),
    path("accounts/", include("accounts.urls")),
    path("cart/", include("cart.urls")),
    path("", include("catalog.urls")),
]
