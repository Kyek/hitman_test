from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.password_validation import validate_password
from .models import Hitman

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': 'johndoe@example.com',
            'id': 'username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input',
            'placeholder': '',
            'id': 'password',
        }), validators=[validate_password])


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': 'johndoe@example.com',
            'id': 'username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input',
            'placeholder': '',
            'id': 'password',
        }))

    class Meta:
        model = Hitman
        fields = ["email", "password"]
