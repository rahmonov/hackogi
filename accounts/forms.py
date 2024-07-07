from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import TextInput, EmailInput, PasswordInput
from accounts.models import CustomUser


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Username'
        })
        self.fields['password'].widget = PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Password'
        })

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Email'
        })
        self.fields['password1'].widget = PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Password',
            'id': 'password1'
        })
        self.fields['password2'].widget = PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Password Confirmation',
            'id': 'password2'
        })

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "password1",
            "password2"
        )
