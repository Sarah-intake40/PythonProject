"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Post/',include('Post.urls')),
    path('adminIndex',views.index),
    path('user/<id>',views.viewUser),
    path('users',views.all_users),
    path('post/<id>',views.viewPost),
    path('posts',views.all_posts),
    path('cats',views.all_cats),
    path('cat/<id>',views.viewCat),
    path('addUser',views.addUser),
    path('addCat',views.addCat),
    path('addPost',views.addpost),
    path('updateUser/<id>',views.updateUser),
    path('updateCat/<id>',views.updateCat),
    path('updatePost/<id>',views.updatePost),
    path('deleteUser/<id>',views.delete),
    path('deleteCat/<id>',views.deleteCat),
    path('deletePost/<id>',views.deletePost),
    path('blockUser/<id>',views.blockUser),
    path('unblockUser/<id>',views.unblockUser),
    path('setadmin/<id>',views.setAdmin),
    path('words',views.all_words),
    path('addWord',views.addWord),
    path('deleteWord/<id>',views.deleteWord),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
