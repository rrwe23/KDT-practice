from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.

# 요청 정보를 받아서
def index(request):

    articles = Articles.objects.order_by("-pk")

    context = {
        "articles": articles,
    }

    # 페이지를 렌더
    return render(request, "articles/index.html", context)


def new(request):
    return render(request, "articles/new.html")


def create(request):
    # DB 에 저장하는 로직
    title = request.GET.get("title")
    content = request.GET.get("content")
    Articles.objects.create(title=title, content=content)
    return redirect("articles:index")
