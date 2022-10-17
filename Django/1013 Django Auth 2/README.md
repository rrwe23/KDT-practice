## 📗이미지 업로드

***

>  이미지 업로드를 위해 어떤기능을 구현해야 할까?

`pillow`

- 이미지를 관리하는 파이썬 이미지 라이브러리

install pillow

```python
pip install pillow
```

models.py 설계

```python
class Article(models.Model)
    title = modles.CharField(max_length=20)
.
.
.

    image = models.ImageField(upload_to='images/', blank=True)
# black = True를 통해 이미지 필드에 빈 값이 허용되도록 한다.
```

이후 `makemigrations`, `migrate`

```python
python manage.py makemigrations


python manage.py migrate
```

`이후  forms.py 구현`

```python
# forms.py
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','image'] # 불러올 값 입력
```

`URL 설정`

- enctype(인코딩) 속성을 반드시 지정

- <input type="file"을 사용할 경우에 사용

```python
# html
<form action="" method="POST" enctype="multipart/form-data" >
        {% csrf_token %}
        {% bootstrap_form article_form %}
        {% bootstrap_button content="글쓰기" button_type="submit" button_class="btn-secondary col-3" %}

    </form>
# <enctype='multipart/form-data'> 추가

<img src="{{ article.image.url }}" alt="{{ article.image }}">
# 업로드 된 파일의 경로는 Django 가 제공하는 URL 속성을 통해 얻을 수 있다.
```

- 사용자가 업로드 한 파일들을 보관할 디렉토리의 절대 경로를 지정

- Django는 성능을 위해 업로드 파일은  DB에 저장하지 않는다.

```python
# settings.py
MEDIA_ROOT = BASE_DIR / 'images'
MEDIA_URL = 'media/' # 비어있지 않은 값으로 설정한다면 반드시 '/'로 끝
```

`views 설정`

- 가장 밖 경로에 media/images 폴더 추가

- images 폴더 안에 사진들을 넣어준다.

```python
# request.FILES 추가
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
```

- article.image.url = 업로드 파일의 경로

- article.image = 업로드 파일의 파일 이름

`image Resizing`

> django-imagekit 라이브러리를 활용한다.

`라이브러리 설치`

```python```
pip install django-imagekit

```
```python
#settings.py

INSTALLED_APP = [
    'imagekit',
]
```

```python
# models.py

# from imagekit.models import ProcessedImageField
# from imagekit.processors import Thumbnail

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='images/',blank=True)
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality':90},
    ) # 추후 값을 변경하더라도 makemigrations 없이 즉시 반영

def __str__(self):
    return self.title
```

## 🤦‍♀️[부록]. Django Secret key 분리

***

그동안 시크릿 키를 수동으로 분리했었는데 구글링을 통해 .gitignore로 관리해야 함을 깨달았다...

우선, 프로젝트 폴더 내에 secrets.json 파일을 생성한다.

```python
# secrets.json
{
  "SECRET_KEY": "<???>"
}
```

이후 settings.py 에서 추가적인 코드를 입력한다.

```python
import os, json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent


secret_file = os.path.join(BASE_DIR, 'secrets.json')  # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")
```

이후 .gitignore 파일에 추가

```memo
# .gitignore 파일

secrets.json
```
