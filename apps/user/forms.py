import datetime

from django import forms
from django.contrib.auth import password_validation
from django.forms import widgets
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.views import get_user_model


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control form-control-lg'}),
    )
    password = forms.CharField(
        label="password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control form-control-lg'}),
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='username',
        widget=widgets.TextInput(attrs={'autofocus': True, 'class': 'form-control form-control-lg'})
    )
    password1 = forms.CharField(
        label="password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control form-control-lg'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="confirm password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control form-control-lg'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']
