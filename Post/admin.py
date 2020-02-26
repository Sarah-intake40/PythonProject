from django.contrib import admin
from .models import post , Category , Comment , Reply

# Register your models here.
admin.site.register(post)
admin.site.register(Category)
admin.site.register(Reply)
admin.site.register(Comment)