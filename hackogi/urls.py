from django.contrib import admin
from django.urls import path, include

from hackogi.views import home_page

urlpatterns = [
    path("", home_page, name="home"),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path('admin/', admin.site.urls),
]
