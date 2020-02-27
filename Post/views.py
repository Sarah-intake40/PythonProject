from django.shortcuts import render
import datetime
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from Post.models import Category, post ,Comment
from Post.form import CommentForm , ReplyForm
from django.core.exceptions import  ValidationError

        


def all_categories(request):
    all_cat = Category.objects.all()
    context = {'all_cat' : all_cat}
    return render (request , 'Post/single.html' , context)




def post_by_category(request,Id):
    cat = Category.objects.get(id=Id)
    posts = post.objects.filter(Category_id=cat)
    context = {'all_post_inCat' :posts,
    'CatName':cat }
    return render (request , 'Post/travel.html' , context)
 
def show_comments(request,Id):
   
    Post = post.objects.filter(id=Id)
    comment = Comment.objects.filter(owner=Id)
    count = comment.count()
  
    if request.method == 'POST':
       
        form = CommentForm(request.POST)
        


        if (form.is_valid()):
            new_comment = form.save(commit=False)

            new_comment.post = Post
            new_comment.name = request.user
            print("dasxasxsazd",new_comment)
            new_comment.save()
            return HttpResponseRedirect("/Post/onePost")
        # else:
        #     print("zsadaza")
        #     raise ValidationError(('Invalid Value') , code='invalid')
    else:
        form = CommentForm()
    context = {'Post' : Post
    ,'all_comments' : comment,'count':count,'form':form}
    return render (request , 'Post/onePost.html' , context)

def all_posts(request):
    
    all_post = post.objects.all().order_by("post_date").reverse()
    all_cat = Category.objects.all()
    if len(all_post)<=5:
        context = {'all_cat' : all_cat,'all_post' : all_post}
    else:
        fivePosts=all_post[:5]
        context = {'all_cat' : all_cat,'all_post' : fivePosts}
    return render (request , 'Post/single.html' , context)
    


 

# def add_comment(request,text,post_id):
    # if request.method == 'POST':
    #     comment
        
    #     u = request.user
         
    #     comment = Comment.objects.create(text=text, post=Post.objects.get(id=post), username=u,
    #                                  )
    #     comment.save()
    #     return HttpResponseRedirect("/Post/onePost")


        


# def show_reply(request, post_id, comment_id):
#     bad_words = BadWords.objects.all()
#     reply = Reply.objects.filter(post=Post.objects.get(id=post_id), comment=Comment.objects.get(id=comment_id))
#     reply = replaceBadWord(reply, bad_words)
#     return JsonResponse(serializers.serialize('json', reply), safe=False)


# def add_reply(request, text, post_id, comment_id):
#     date = datetime.datetime.now()
#     u = request.user
#     bad_words = BadWords.objects.all()
#     reply = Reply.objects.create(text=text, comment=Comment.objects.get(id=comment_id),
#     post=Post.objects.get(id=post_id), username=u, created_date=date)
#     reply = replaceBadWord([reply], bad_words)
#     return JsonResponse(serializers.serialize('json', reply), safe=False)


# def search(request, term):
#     cat = Post.objects.filter(Q(title__icontains=term) | Q(tags=Tag.objects.filter(name__icontains=term)))
#     return JsonResponse(serializers.serialize('json', cat), safe=False)


# def show_likes(request, post_id):
#     like = Likes.objects.filter(post_id=post_id).count()
#     return JsonResponse(like, safe=False)


# def show_dislikes(request, post_id):
#     dislike = Dislikes.objects.filter(post_id=post_id).count()
#     return JsonResponse(dislike, safe=False)


# def add_like(request, post_id):
#     u = request.user.id
#     like = Likes.objects.filter(post_id=post_id, user_id=u)
#     if (like.exists()):
#         like.delete()
#         result = 'unlike'
#     else:
#         like = Likes.objects.create(post_id=post_id, user_id=u)
#         result = 'like'
#     return JsonResponse(result, safe=False)


# def add_dislike(request, post_id):
#     u = request.user.id
#     dislike = None
#     try:
#         dislike = Dislikes.objects.get(post_id=post_id, user_id=u)
#     except:
#         pass
#     if (dislike):
#         dislike.delete()
#         result = 'undislike'
#     else:
#         dislike = Dislikes.objects.create(post_id=post_id, user_id=u)
#         dislikeCounter = Dislikes.objects.filter(post_id=post_id).count()
#         if dislikeCounter == 10:
#             Post.objects.get(id=post_id).delete()
#             result = 'deletePost'
#         else:
#             result = 'dislike'
#     return JsonResponse(result, safe=False)














