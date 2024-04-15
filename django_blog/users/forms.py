from django import forms
from django.contrib.auth.forms import  User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 
"""
we are creating a custom user form beacuse usercreation form 
dosenot have email field. when an instance of userregisterfrom is save,
it will save to User model as metion in meta class.
"""
class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    
    class Meta():
        model= User
        fields = ['username', 'email','password1', 'password2']
        
""" this form allows us to update user info"""       
class UserUpdateForm(forms.ModelForm):
    email= forms.EmailField()
    
    class Meta():
        model= User
        fields = ['username', 'email']
        
"""this foram allow us to update profile image """       
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta():
        model= Profile
        fields = ['image']