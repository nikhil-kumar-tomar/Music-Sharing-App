from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *

class user_create(UserCreationForm):
    first_name=forms.CharField(max_length=300,required=True)
    last_name=forms.CharField(max_length=300,required=True)
    class Meta():
        model=get_user_model()
        fields=['username','first_name','last_name','email','password1','password2']
class user_sign(forms.Form):
    email=forms.CharField(max_length=400)
    password=forms.CharField(max_length=400)