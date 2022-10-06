from django.shortcuts import render,redirect
from . models import Article


def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request,'articles/index.html', context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    title = request.GET.get("title")
    summary = request.GET.get('summary')
    running_time = request.GET.get('running_time')
    Article.objects.create(title=title,summary=summary,running_time=running_time)
    return redirect('articles:index')

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }

    return render(request,'articles/detail.html',context)


def update(request,pk):
    article = Article.objects.get(pk=pk)

    
    summary = request.GET.get('summary')
    

   
    article.summary = summary
   
    article.save()

    return redirect('articles:index')

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

