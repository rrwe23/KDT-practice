
# accounts/views.py 에서 detail 함수 작성

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import logout as auth_logout

def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)

def signup(request):
    # POST 요청 처리
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:     
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    # user 정보 받아오기
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

def login(request):
     if request.user.is_anonymous:
        if request.method == 'POST':
            # AuthenticationForm은 ModelForm 이 아님!
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                # 세션에 저장
                # login 함수는 request, user 객체를 인자로 받음
                # user 객체는 form 에서 인증된 유저 정보
                auth_login(request, form.get_user()) 
                return redirect('accounts:index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form
    }
        return render(request,'accounts/login.html',context)
     else:
        return redirect('accounts:index')

def logout(request):
    auth_logout(request)
    return redirect('index')


