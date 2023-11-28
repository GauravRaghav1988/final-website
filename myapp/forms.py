from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from .models import *



from django import forms
from .models import BlogPost

class SignUpForm(UserCreationForm):
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'email': 'Email'}



class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['heading', 'user_name', 'content','post_number']









