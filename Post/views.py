from django.shortcuts import render


#from __future__ import unicode_literals
import datetime
import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
#from pyapp.forms import SignUpForm
#from pyapp.models import *
#from django.shortcuts import render_to_response
#from pyblog.settings import BASE_DIR
#from django.contrib.auth.decorators import login_required
#from django.db.models import Q
from Post.models import Category, post ,Comment

# Create your views here.


def all_categories(request):
    all_cat = Category.objects.all()
    # for post in all_post:
    #     post.dir = BASE_DIR
    context = {'all_cat' : all_cat}
    # return JsonResponse(serializers.serialize('json', all_post), safe=False)
    return render (request , 'Post/single.html' , context)




def post_by_category(request,Id):
    cat = Category.objects.get(id=Id)
    posts = post.objects.filter(Category_id=cat)
     


    # post_id=posts.objects.filter(id=owner)


    # comm= Comment.objects.filter(owner=post_id)
    # iterate = comm.count()
    context = {'all_post_inCat' :posts,
    'CatName':cat }
    return render (request , 'Post/onePost.html' , context)


def show_post(request, post_id):
    post = Post.objects.filter(id=post_id).order_by('-created_date')
    return JsonResponse(serializers.serialize('json', post), safe=False)



def CharStars(text):
    char_no = len(text)
    stars = ""
    while char_no != 0:
        stars += '*'
        char_no -= 1
    return stars


def replaceBadWord(comment, bad_words):
    for word in bad_words:
        for ct in comment:
            bad_word = str(word).lower()
            my_comment = ct.text.lower()
            stars = CharStars(bad_word)
            ct.text = my_comment.replace(bad_word, str(stars))
    return comment




def show_comments(request, post_id):
    comment = Comment.objects.filter(post_id=post_id).order_by('-created_date')
    bad_words = BadWords.objects.all()
    comment = replaceBadWord(comment, bad_words)
    return JsonResponse(serializers.serialize('json', comment), safe=False)

def all_posts(request):
    all_post = post.objects.all()
   
    
    all_cat = Category.objects.all()
    
    context = {'all_cat' : all_cat
    ,'all_post' : all_post}
    return render (request , 'Post/single.html' , context)
    


 

def add_comment(request, text, post):
    date = datetime.datetime.now()
    u = request.user
    comment = Comment.objects.create(text=text, post=Post.objects.get(id=post), username=u,
                                     created_date=date)
    bad_words = BadWords.objects.all()
    comment = replaceBadWord([comment], bad_words)
    return JsonResponse(serializers.serialize('json', comment), safe=False)


def show_reply(request, post_id, comment_id):
    bad_words = BadWords.objects.all()
    reply = Reply.objects.filter(post=Post.objects.get(id=post_id), comment=Comment.objects.get(id=comment_id))
    reply = replaceBadWord(reply, bad_words)
    return JsonResponse(serializers.serialize('json', reply), safe=False)


def add_reply(request, text, post_id, comment_id):
    date = datetime.datetime.now()
    u = request.user
    bad_words = BadWords.objects.all()
    reply = Reply.objects.create(text=text, comment=Comment.objects.get(id=comment_id),
    post=Post.objects.get(id=post_id), username=u, created_date=date)
    reply = replaceBadWord([reply], bad_words)
    return JsonResponse(serializers.serialize('json', reply), safe=False)


def search(request, term):
    cat = Post.objects.filter(Q(title__icontains=term) | Q(tags=Tag.objects.filter(name__icontains=term)))
    return JsonResponse(serializers.serialize('json', cat), safe=False)


def show_likes(request, post_id):
    like = Likes.objects.filter(post_id=post_id).count()
    return JsonResponse(like, safe=False)


def show_dislikes(request, post_id):
    dislike = Dislikes.objects.filter(post_id=post_id).count()
    return JsonResponse(dislike, safe=False)


def add_like(request, post_id):
    u = request.user.id
    like = Likes.objects.filter(post_id=post_id, user_id=u)
    if (like.exists()):
        like.delete()
        result = 'unlike'
    else:
        like = Likes.objects.create(post_id=post_id, user_id=u)
        result = 'like'
    return JsonResponse(result, safe=False)


def add_dislike(request, post_id):
    u = request.user.id
    dislike = None
    try:
        dislike = Dislikes.objects.get(post_id=post_id, user_id=u)
    except:
        pass
    if (dislike):
        dislike.delete()
        result = 'undislike'
    else:
        dislike = Dislikes.objects.create(post_id=post_id, user_id=u)
        dislikeCounter = Dislikes.objects.filter(post_id=post_id).count()
        if dislikeCounter == 10:
            Post.objects.get(id=post_id).delete()
            result = 'deletePost'
        else:
            result = 'dislike'
    return JsonResponse(result, safe=False)














