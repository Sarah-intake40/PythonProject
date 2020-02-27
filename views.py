from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import post,Category,forbWords
from .forms import UserForm,PostForm,CategoryForm,wordForm
from django.db import transaction
from django.contrib.auth.models import User


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
    # return JsonResponse(serializers.serialize('json', posts), safe=False)
    context = {'all_post_inCat' :posts,
    'CatName':cat}

     
    # return JsonResponse(serializers.serialize('json', all_post), safe=False)
  return render (request , 'Post/travel.html' , context)


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
    # for post in all_post:
    #     post.dir = BASE_DIR
    
    all_cat = Category.objects.all()
    # for post in all_post:
    #     post.dir = BASE_DIR
    context = {'all_cat' : all_cat
    ,'all_post' : all_post}

    # return JsonResponse(serializers.serialize('json', all_post), safe=False)
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


