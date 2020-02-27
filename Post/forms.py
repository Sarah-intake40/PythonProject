from django import forms
from .models import Category,post,forbWords
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']


class PostForm(forms.ModelForm):
    class Meta:
        model=post
        fields=['title','content','post_date','Owner','Category_id','image']
    
class wordForm(forms.ModelForm):
    class Meta:
        model=forbWords
        fields=['word']



    
    

