from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView

app_name = "accounts"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout-view"),
]

