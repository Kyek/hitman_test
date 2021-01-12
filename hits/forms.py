from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.password_validation import validate_password
from .models import Hitman, Hit


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': 'johndoe@example.com',
            'id': 'username'
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': '',
            'id': 'password',
        }),
        validators=[validate_password])


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': 'johndoe@example.com',
            'id': 'username'
        }))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['class'] = 'input'

    class Meta:
        model = Hitman
        fields = ["email"]


class HitForm(forms.ModelForm):
    class Meta:
        model = Hit
        fields = ["description", "target_name", "asignee"]

    def __init__(self, *args, **kwargs):
        super(HitForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "input"

    def save(self, **kwargs):
        self.instance.created_by = kwargs["created_by"]
        return super(HitForm, self).save()


class HitDetailForm(forms.ModelForm):
    class Meta:
        model = Hit
        fields = [
            "description", "target_name", "asignee", "created_by", "status"
        ]
