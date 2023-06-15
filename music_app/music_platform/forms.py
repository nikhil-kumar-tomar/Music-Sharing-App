from typing import Any
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

class music_upload_form(forms.ModelForm):
    choices = [
    ('public', 'Public'),
    ('protected', 'Protected'),
    ('private', 'Private')
    ]
    music_name=forms.CharField(max_length=300)
    music_type=forms.ChoiceField(choices=choices)
    protected_access_allowed=forms.CharField(max_length=300,required=False)
    owner_email=forms.EmailField(required=False)
    class Meta():
        model=music_uploads_model
        fields=["music_name","music_file","music_type"]
