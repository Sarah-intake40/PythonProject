from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import datetime

from CommandNotFound.db import db
from django.db import models
from django.contrib.auth.models import User




#from django.contrib.auth.models import AbstractUser



# Create your models here.


# class person(models.Model):
#     name=models.CharField(max_length=40)
#     email=models.CharField(max_length=50)
#     password=models.CharField(max_length=40)
#     profile_picture = models.ImageField()
#     birth_date = models.DateField(null=True, blank=True)
#     flag_admin = models.CharField(max_length=1, blank=True)
#     flag_blocked = models.CharField(max_length=1, blank=True)
#     flag_login = models.CharField(max_length=1, blank=True)

#     def isAdmin(self):
#         if(self.flag_admin == '1'):
#             return True
#         else:
#             return False
#     isAdmin.boolean=True
#     isAdmin.short_description='One of the staff'
#     def isBlocked(self):
#         if(self.flag_blocked == '1'):
#             return True
#         else:
#             return False

#     def isActive(self):
#         if(self.flag_login == '1'):
#             return True
#         else:
#             return False


#     def __str__(self):
#         return self.name
#     class Meta:
#         unique_together = ('email','name')
     

class Category(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name


class post(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now, null=False)
    image = models.ImageField(default='default.jpg',  upload_to='open_img/',null=True)
    Owner=models.ForeignKey(User,on_delete=models.DO_NOTHING)    
    #counter = db.Column(db.Integer, nullable=True)
    #Category_id = db.Column(db.Integer, db.ForeignKey('Category.id'), nullable=False)
    Category_id = models.ForeignKey(Category,null = True ,on_delete=models.SET_NULL)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    owner = models.ForeignKey(post, on_delete=models.CASCADE)
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False) 
    posts = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')



class Reply(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    owner = models.ForeignKey(Comment, on_delete=models.CASCADE)
    body = models.TextField()
    reply_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False) 
    

class forbWords(models.Model):
    word=models.CharField(max_length=50)

