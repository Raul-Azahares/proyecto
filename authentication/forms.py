from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput

from authentication.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-user",
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        label="Password ",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-user",
                'placeholder': 'Password',
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-user",
                'placeholder': 'Username',
            }
        )
    )
    email = forms.CharField(
        label="Email ",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control form-control-user",
                'placeholder': 'Email Address',
            }
        )
    )
    password1 = forms.CharField(
        label="Password ",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-user",
                'placeholder': 'Password',
            }
        )
    )
    password2 = forms.CharField(
        label="Repeat your password ",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-user",
                'placeholder': 'Repeat Password',
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['calle','num_ext','num_int','phone_num']
        widgets = {

            "calle": TextInput(attrs={"class": "form-control"}),
            "num_ext": TextInput(attrs={"class": "form-control"}),
            "num_int": TextInput(attrs={"class": "form-control"}),
            "phone_num": TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "calle": "Calle",
            "num_ext": "Numero de extension",
            "num_int": "Numero de interior",
            "phone_num": "Telefono",
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
