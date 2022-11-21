from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email')

class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['username','password','remember_me']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio']

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email']