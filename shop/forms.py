from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
    label="",
    max_length=30,
    required=True,
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Please enter your first name'
    })
    )
    last_name = forms.CharField(
    label="",
    max_length=30,
    required=True,
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Please enter your last name'
    })
    )
    
    email = forms.EmailField (
    label="",
    required=True,
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Please enter your email'
    })
    )
    
    user_name = forms.CharField(
    label="",
    max_length=20,
    required=True,
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Please enter your user name'
    })
    )
    
    password1 = forms.CharField(
    label="",
    max_length=30,
    required=True,
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'name' : 'password',
        'type' : 'password',
        'placeholder': 'Enter a password of at least 8 characters.'
    })
    )
    
    password2 = forms.CharField(
    label="",
    max_length=30,
    required=True,
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'name' : 'password',
        'type' : 'password',
        'placeholder': 'Enter your password again.'
    })
    )


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'user_name','password1', 'password2')

