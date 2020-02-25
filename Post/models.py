from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import datetime

from CommandNotFound.db import db
from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100, null=False , default='General')

    def __str__(self):
        return self.name


class post(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=100, null=False,default=' ')
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', upload_to='open_img/',null=False)
    #counter = db.Column(db.Integer, null=True)
    Category_id = models.ForeignKey(Category,null = True ,on_delete=models.SET_NULL)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title



