from django import forms
from .models import person,Category,post,forbWords

class UserForm(forms.ModelForm):
    class Meta:
        model=person
        fields=['name','email','password','flag_admin']


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']


class PostForm(forms.ModelForm):
    class Meta:
        model=post
        fields=['title','content','post_date','Owner','postCat','image']
    
class wordForm(forms.ModelForm):
    class Meta:
        model=forbWords
        fields=['word']



    
    
