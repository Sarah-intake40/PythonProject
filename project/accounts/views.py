# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout



from accounts.forms import SignUpForm


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})



#
# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#
#         if form.is_valid():
#             # flag = request.user.is_active
#             # if flag:
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#         # else:
#              # messages.warning(request, 'sryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
#
#     else:
#         form = LoginForm()
#     return render(request, 'registration/login.html', {
#         'form': form,
#     })

# def logout_user(request):
#     logout(request)
#     return render(request, 'registration/logout.html', {
#
#     })


