from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True, label='Full Name')
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2']
        
class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
