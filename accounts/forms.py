from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser  # Import CustomUser model

# Custom User Creation Form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use CustomUser instead of User
        fields = ['username', 'password1', 'password2', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

# Custom User Login Form
class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser  # Use CustomUser if you have a custom user model
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
