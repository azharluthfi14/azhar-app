from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from .validators import validate_unique_email, validate_unique_username


class user_form_create(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, validators=[
                               validate_unique_username])
    email = forms.EmailField(required=True, label='Email address', validators=[
                             validate_unique_email])
    password1 = forms.CharField(required=True, label='Password')
    password2 = forms.CharField(required=True, label='Password confirmation')

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]

    username.widget = forms.TextInput(
        attrs={'class': 'signupForm', 'placeholder': 'Enter your username.'})
    email.widget = forms.EmailInput(
        attrs={'class': 'signupForm', 'placeholder': 'Enter your valid email addres.', 'data-placement': 'top', 'data-content': 'Must be a valid e-mail address'})
    password1.widget = forms.PasswordInput(
        attrs={'class': 'signupForm', 'placeholder': 'Min 8 characters.', 'data-placement': 'bottom'})
    password2.widget = forms.PasswordInput(
        attrs={'class': 'signupForm', 'placeholder': 'Confirm your password'})


class form_user_update(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email address')
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']

    email.widget = forms.EmailInput(
        attrs={'class': 'edit_email'})
    username.widget = forms.TextInput(
        attrs={'class': 'edit_username'})
    first_name.widget = forms.TextInput(
        attrs={'class': 'edit_username '})
    last_name.widget = forms.TextInput(
        attrs={'class': 'edit_username'})


class form_user_update_avatar(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['image']
    image.widget = forms.FileInput(attrs={'class': 'image-upload'})
