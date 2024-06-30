from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from accounts.models import CustomUser


class CustomLoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "password1",
            "password2"
        )

