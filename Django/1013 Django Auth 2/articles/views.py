from django.shortcuts import render,redirect

from articles.forms import ArticleForm
from articles.models import Article

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request,'articles/index.html',context)


def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST,request.FILES)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form' : article_form
    }

    return render(request,'articles/new.html',context=context)


def detail(request,pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article

    }

    return render(request,'articles/detail.html',context)


def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method =='POST':
        article_form = ArticleForm(request.POST,instance = article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail',article.pk)
    else:
        article_form = ArticleForm(instance = article)
    context = {
        'article_form' : article_form
    }
    return render(request,'articles/update.html',context)

# render = 원하는 인자를 html 템플릿으로 넘길 수 있다.
# redirect = URL 로 이동
def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')



