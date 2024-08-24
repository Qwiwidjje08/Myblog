from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from . import models
from django.contrib.auth.models import User


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password','password2')
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blogs
        fields = ('category','title','text','image1','image2','image3')
