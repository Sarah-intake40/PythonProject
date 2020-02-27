from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import post,Category,forbWords
from .forms import UserForm,PostForm,CategoryForm,wordForm
from django.db import transaction
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    all_users = User.objects.all()
    all_posts = post.objects.all()
    all_cats = Category.objects.all()
    all_words=forbWords.objects.all()
    context = {'all_users':all_users,'all_posts':all_posts,'all_cats':all_cats,'all_words':all_words}
    return render(request,'base_site.html',context)


def viewUser(request,id):
    user=User.objects.get(id=id)
    context={'user':user}
    return render(request,'viewUser.html',context)


def blockUser(request,id):
    user=User.objects.get(id=id)
    user.is_active= '0'
    user.save()
    transaction.commit()
    return HttpResponseRedirect('/users')


def unblockUser(request,id):
    user=User.objects.get(id=id)
    user.is_active=  1 
    user.save()
    transaction.commit()
    return HttpResponseRedirect('/users')


def all_users(request):
    all_users =User.objects.all()
    context = {'all_users':all_users}
    return render(request,'all_users.html',context)

def addUser(request):
    user=UserForm()
    if(request.method=='POST'):
        user=UserForm(request.POST)
        if(user.is_valid()):
            user.save()
            return HttpResponseRedirect('/users')
    else:
        context={'user':user}
        return render (request,'userForm.html',context)

def updateUser(request,id):
    user=User.objects.get(id=id)
    if(request.method=='POST'):
        user_form=UserForm(request.POST,instance=user)
        if(user_form.is_valid()):
            user_form.save()
            return HttpResponseRedirect('/users')
    else:
        user_form=UserForm(instance=user)
        context={'user':user_form}
        return render(request,'userForm.html',context)

def delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect('/users')

def setAdmin(request,id):
    user=User.objects.get(id=id)
    if(user.is_active == 0):
        user.is_active = 1
        user.is_staff =  1
        user.save()
        transaction.commit()
        return HttpResponseRedirect('/users')
    else:
        user.is_staff = 1
        user.save()
        transaction.commit()
        return HttpResponseRedirect('/users')

#POST

def viewPost(request,id):
    wantedPost=post.objects.get(id=id)
    context={'post':wantedPost}
    return render(request,'viewPost.html',context)

def all_posts(request):
    all_posts = post.objects.all()
    context = {'all_posts':all_posts}
    return render(request,'all_posts.html',context)

def addpost(request):
    post=PostForm()
    if(request.method=='POST'):
        post=PostForm(request.POST)
        if(post.is_valid()):
            post.save()
            return HttpResponseRedirect('/posts')
    else:
        context={'post':post}
        return render (request,'postform.html',context)

def updatePost(request,id):
    wantedPost=post.objects.get(id=id)
    if(request.method=='POST'):
        post_form=PostForm(request.POST,instance=wantedPost)
        if(post_form.is_valid()):
            post_form.save()
            return HttpResponseRedirect('/posts')
    else:
        post_form=PostForm(instance=wantedPost)
        context={'post':post_form}
        return render(request,'postform.html',context)

def deletePost(request,id):
    WantedPost=post.objects.get(id=id)
    WantedPost.delete()
    return HttpResponseRedirect('/posts')


#Category

def viewCat(request,id):
    cat=Category.objects.get(id=id)
    context={'cat':cat}
    return render(request,'viewCat.html',context)

def all_cats(request):
    all_cats = Category.objects.all()
    context = {'all_cats':all_cats}
    return render(request,'all_cats.html',context)

def addCat(request):
    cat=CategoryForm()
    if(request.method=='POST'):
        cat=CategoryForm(request.POST)
        if(cat.is_valid()):
            cat.save()
            return HttpResponseRedirect('/cats')
    else:
        context={'cat':cat}
        return render (request,'catform.html',context)

def updateCat(request,id):
    cat=Category.objects.get(id=id)
    if(request.method=='POST'):
        cat_form=CategoryForm(request.POST,instance=cat)
        if(cat_form.is_valid()):
            cat_form.save()
            return HttpResponseRedirect('/cats')
    else:
        cat_form=CategoryForm(instance=cat)
        context={'cat':cat_form}
        return render(request,'catform.html',context)

def deleteCat(request,id):
    cat=Category.objects.get(id=id)
    cat.delete()
    return HttpResponseRedirect('/cats')
#add admin

def addAdmin(request): 
    admin=UserForm()
    if(request.method=='POST'):
        admin=UserForm(request.POST)
        if(admin.is_valid()):
            admin.save()
            return HttpResponseRedirect('/users')
    else:
        context={'admin':admin}
        return render (request,'adminform.html',context)       
#words
def all_words(request):
    words=forbWords.objects.all()
    context={'words':words}
    return render(request,'all_words.html',context)

def addWord(request):
    word=wordForm()
    if(request.method=='POST'):
        word=wordForm(request.POST)
        if(word.is_valid()):
            word.save()
            return HttpResponseRedirect('/words')
    else:
        context={'word':word}
        return render (request,'wordForm.html',context)


def deleteWord(request,id):
    word=forbWords.objects.get(id=id)
    word.delete()
    return HttpResponseRedirect('/words')


