from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser  # Import CustomUser model


from django import forms
from .models import Trainer

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



# forms.py


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'experience', 'specialty', 'bio']


from django import forms
from .models import Fitness

class FitnessForm(forms.ModelForm):
    class Meta:
        model = Fitness
        fields = ['name', 'trainer', 'description', 'duration_weeks', 'difficulty_level']
        widgets = {
            'trainer': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'duration_weeks': forms.NumberInput(attrs={'class': 'form-control'}),
            'difficulty_level': forms.Select(attrs={'class': 'form-select'})
        }


