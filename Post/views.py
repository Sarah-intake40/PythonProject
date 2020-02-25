from django.shortcuts import render



import datetime
import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from Post.models import Category, post 

# Create your views here.


def all_categories(request):
    all_cat = Category.objects.all()
    # cats = []
    # for cat in all_cat:
    #     cats.append({"state": is_supped(request, cat), "cat": serializers.serialize('json', [cat])})
    # #return JsonResponse(json.dumps(cats), safe=False)
    context = {'all_cat' : all_cat}
    return render (request , 'Post/single.html' , context)




def post_by_category(request, name):
    cat = Category.objects.get(cat_name=name)
    posts = Post.objects.filter(category=cat).order_by('-created_date')
    context = {'posts' : posts}
    #return JsonResponse(serializers.serialize('json', posts), safe=False)
    return render (request , 'Post/----.html' , context)

def show_post(request, post_id):
    post = Post.objects.filter(id=post_id).order_by('-created_date')
    context = {'post' : post}
    #return JsonResponse(serializers.serialize('json', post), safe=False)
    return render (request , 'Post/----.html' , context)



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





def all_posts(request):
    all_post = post.objects.all()
    # for post in all_post:
    #     post.dir = BASE_DIR
    all_cat = Category.objects.all()
    context = {'all_cat' : all_cat ,
                'all_post' : all_post}
    return render (request , 'Post/single.html' , context)



def get_category(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    #return JsonResponse(serializers.serialize('json', [cat]), safe=False)
    context = {'cat' : cat}
    return render (request , 'Post/----.html' , context)














