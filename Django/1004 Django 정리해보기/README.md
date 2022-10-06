## Django CRUD?

***

- Django?
  
  - 파이썬 기반 웹 프레임워크
  
  - URL 요청을 받아서  &rarr; 처리하고(views.py) &rarr; 응답을 해준다.(Template)
  
  - MTV(Model, Template, View)

- Django CRUD 시작하기 전에...
  
  - 가상환경 폴더를 ```.gitignore``` 로 설정을 해둔다.
  
  - 가상환경을 생성해준다.
  
  - Scripts/activate를 실행하여 가상환경 시작
  
  - ```text```
    $ python -m venv venv(가상환경 이름) # 가상환경 생성
    $ source venv/scripts/activate # 가상환경 실행
    
    # (venv) $
    
    $ pip install django==3.2.13 # Django LTS 버전 설치
    $ pip freeze > requirements.txt # 기록지 생성
    
    ```
    
    ```
  
  Django 프로젝트 생성 및 실행

```textile
$ django-admin startproject pjt .(프로젝트명) # Django 프로젝트 생성
$ python manage.py startapp practice(애플리케이션 이름) # 앱 생성
$ python manage.py runserver # 앱 실행
```

앱 생성 이후 앱 등록 ( settings.py)

```textile
INSTALLED_APPS = [
    'articles',
]
```

프로젝트 폴더 속 urls.py 에 include 를 추가

```textile
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/", include("articles.urls")),
]
```

앱 폴더에 urls.py 파일을 생성하고 다음과 같이  설정

```python
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # http://localhost:8000/articles/
    path("", views.index, name="index"),
]   
```

이후 views.py 함수를 구성

```python
from django.shortcuts import render

# Create your views here.

# 요청 정보를 받아서
def index(request):

    # 페이지를 렌더
    return render(request, "articles/index.html")  
```

 앱 폴더 내에 templates 폴더 생성, 내부에 앱 이름으로 폴더,index.html 추가

## Model 정의

***

클래스 정의

```python
from django.db import models

# 모델 설계(DB 스키마 설계)
class Articles(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

마이그레이션 파일 생성

```py
python manage.py makemigrations
```

migrate

- DB 반영 완료

```python
python manage.py migrate
```

### crud 기능 구현

***

> 사용자에게  HTML form 제공, 입력한 데이터를 처리

HTML form 제공

> http://127.0.0.1:8000/articles/new/

views.py

```python
from django.shortcuts import render

# Create your views here.

# 요청 정보를 받아서
def index(request):

    # 페이지를 렌더
    return render(request, "articles/index.html")


def new(request):
    return render(request, "articles/new.html")
```

urls.py

```python
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # http://localhost:8000/articles/
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
]
```

new.html 생성

```html
<h1>글쓰기</h1>>

<!-- form : 사용자에게 양식을 제공하고
    값을 받아서(input value)
    서버에 전송(action)-->

<form action="/articles/create/">
    <input type='text' name="title" id="title">
    <label for="content">내용 : </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea>
    <input type="submit" value="글쓰기">

</form>
```

DB 에 저장하는 로직을 만들려고 한다.

views.py

```python
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# 요청 정보를 받아서
def index(request):

    # 페이지를 렌더
    return render(request, "articles/index.html")


def new(request):
    return render(request, "articles/new.html")


def create(request):
    # DB 에 저장하는 로직
    title = request.GET.get("title")
    content = request.GET.get("content")
    Article.objects.create(title=title, content=content)
    return redirect("articles:index")
```

urls.py

```python
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # http://localhost:8000/articles/
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
```

index.html 에서 다음을 통해 게시판 기능 구현

```python
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h1> 게시판</h1>
    <a href="{% url 'articles:new' %}">글 쓰기</a>

</body>

</html>
```

게시글 목록

- DB에서 게시글을 가져와서 template에 전달

```python
# 요청 정보를 받아서
from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.

# 요청 정보를 받아서
def index(request):

    articles = Articles.objects.all()

    context = {
        "articles": articles,
    }

    # 페이지를 렌더
    return render(request, "articles/index.html", context)dex.html")
```

HTML 에서 반복문 작성

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h1> 게시판</h1>
    <a href="{% url 'articles:new' %}">글 쓰기</a>

    {% for article in articles %}
    <h3> {{ article.title }}</h3>
    <p> {{ article.created_at }} | {{ article.updated_at }}</p>
    <hr>
    {% endfor %}

</body>

</html>
```

| POST | 기록  |
| ---- | --- |
| GET  | 조회  |

## Django ModelForm

***
