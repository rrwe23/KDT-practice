## πμ΄λ―Έμ§ μλ‘λ

***

>  μ΄λ―Έμ§ μλ‘λλ₯Ό μν΄ μ΄λ€κΈ°λ₯μ κ΅¬νν΄μΌ ν κΉ?

`pillow`

- μ΄λ―Έμ§λ₯Ό κ΄λ¦¬νλ νμ΄μ¬ μ΄λ―Έμ§ λΌμ΄λΈλ¬λ¦¬

install pillow

```python
pip install pillow
```

models.py μ€κ³

```python
class Article(models.Model)
    title = modles.CharField(max_length=20)
.
.
.

    image = models.ImageField(upload_to='images/', blank=True)
# black = Trueλ₯Ό ν΅ν΄ μ΄λ―Έμ§ νλμ λΉ κ°μ΄ νμ©λλλ‘ νλ€.
```

μ΄ν `makemigrations`, `migrate`

```python
python manage.py makemigrations


python manage.py migrate
```

`μ΄ν  forms.py κ΅¬ν`

```python
# forms.py
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','image'] # λΆλ¬μ¬ κ° μλ ₯
```

`URL μ€μ `

- enctype(μΈμ½λ©) μμ±μ λ°λμ μ§μ 

- <input type="file"μ μ¬μ©ν  κ²½μ°μ μ¬μ©

```python
# html
<form action="" method="POST" enctype="multipart/form-data" >
        {% csrf_token %}
        {% bootstrap_form article_form %}
        {% bootstrap_button content="κΈμ°κΈ°" button_type="submit" button_class="btn-secondary col-3" %}

    </form>
# <enctype='multipart/form-data'> μΆκ°

<img src="{{ article.image.url }}" alt="{{ article.image }}">
# μλ‘λ λ νμΌμ κ²½λ‘λ Django κ° μ κ³΅νλ URL μμ±μ ν΅ν΄ μ»μ μ μλ€.
```

- μ¬μ©μκ° μλ‘λ ν νμΌλ€μ λ³΄κ΄ν  λλ ν λ¦¬μ μ λ κ²½λ‘λ₯Ό μ§μ 

- Djangoλ μ±λ₯μ μν΄ μλ‘λ νμΌμ  DBμ μ μ₯νμ§ μλλ€.

```python
# settings.py
MEDIA_ROOT = BASE_DIR / 'images'
MEDIA_URL = 'media/' # λΉμ΄μμ§ μμ κ°μΌλ‘ μ€μ νλ€λ©΄ λ°λμ '/'λ‘ λ
```

`views μ€μ `

- κ°μ₯ λ° κ²½λ‘μ media/images ν΄λ μΆκ°

- images ν΄λ μμ μ¬μ§λ€μ λ£μ΄μ€λ€.

```python
# request.FILES μΆκ°
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

- article.image.url = μλ‘λ νμΌμ κ²½λ‘

- article.image = μλ‘λ νμΌμ νμΌ μ΄λ¦

`image Resizing`

> django-imagekit λΌμ΄λΈλ¬λ¦¬λ₯Ό νμ©νλ€.

`λΌμ΄λΈλ¬λ¦¬ μ€μΉ`

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
    ) # μΆν κ°μ λ³κ²½νλλΌλ makemigrations μμ΄ μ¦μ λ°μ

def __str__(self):
    return self.title
```

## π€¦ββοΈ[λΆλ‘]. Django Secret key λΆλ¦¬

***

κ·Έλμ μν¬λ¦Ώ ν€λ₯Ό μλμΌλ‘ λΆλ¦¬νμλλ° κ΅¬κΈλ§μ ν΅ν΄ .gitignoreλ‘ κ΄λ¦¬ν΄μΌ ν¨μ κΉ¨λ¬μλ€...

μ°μ , νλ‘μ νΈ ν΄λ λ΄μ secrets.json νμΌμ μμ±νλ€.

```python
# secrets.json
{
  "SECRET_KEY": "<???>"
}
```

μ΄ν settings.py μμ μΆκ°μ μΈ μ½λλ₯Ό μλ ₯νλ€.

```python
import os, json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent


secret_file = os.path.join(BASE_DIR, 'secrets.json')  # secrets.json νμΌ μμΉλ₯Ό λͺμ

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting):
    """λΉλ° λ³μλ₯Ό κ°μ Έμ€κ±°λ λͺμμ  μμΈλ₯Ό λ°ννλ€."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")
```

μ΄ν .gitignore νμΌμ μΆκ°

```memo
# .gitignore νμΌ

secrets.json
```

***

## πDjango(sw)

> μ¬κΈ°κΉμ§μ κ³Όμ ...

- μμ²­ - μλ΅

- APP / MTV ν¨ν΄

- λ‘μ§ β Form λ°μ΄ν° λ°μ

- Model (λ¨μΌ νμ΄λΈ)

- κ²μν(CRUD)

- ModelFormκ²μν(IRVD)

- νμκ°μ

- μμ²­ - μλ΅(μΏ ν€-μΈμ)

- λ‘κ·ΈμΈ

## A one - to - many relationship

---

> κ΄κ³ν λ°μ΄ν°λ² μ΄μ€ νλ©΄..? == ν!

`RDB μμμ κ΄κ³`

- 1:1
  
  - μ΄λ¦, λΉλ°λ²νΈ , μ΄λ©μΌ

- 1:N
  
  - μ¬μ©μμ κΈ, λκΈ

- M:N
  
  - λ€μμ£Όμ κ³΅κ°..

`Foreign Key`

- μΈλ ν€

- κ΄κ³ν λ°μ΄ν°λ² μ΄μ€μμ λ€λ₯Έ νμ΄λΈμ νμ μλ³ν  μ μλ ν€

- μ°Έμ‘°λλ νμ΄λΈμ κΈ°λ³Έ ν€λ₯Ό κ°λ¦¬ν΄

- ν€λ₯Ό μ¬μ©νμ¬ λΆλͺ¨ νμ΄λΈμ μ μΌν κ°μ μ°Έμ‘°(μ°Έμ‘° λ¬΄κ²°μ±)

> λκΈ κΈ°λ₯μ κ΅¬ννλ €λ©΄?
> 
> λκΈλͺ©λ‘, λκΈμμ±, λκΈ μμ± κΈ°λ₯ λ±?

`Foreign Key arguments-on_delete`

- μΈλ ν€κ° μ°Έμ‘°νλ κ°μ²΄κ° μ¬λΌμ‘μ λ, μΈλ ν€λ₯Ό κ°μ§ κ°μ²΄λ₯Ό μ΄λ»κ² μ²λ¦¬ν  κ²μΈμ§ μ μ

- on_delete
  
  - CASCADE : λΆλͺ¨ κ°μ²΄(μ°Έμ‘° λ κ°μ²΄)κ° μ¬λΌμ‘μλ, μ΄λ₯Ό μ°Έμ‘°νλ κ°μ²΄λ μ­μ 

`Comment λͺ¨λΈ μ μ`

- μΈλ ν€ νλλ μμΉμ κ΄κ³μμ΄ λ§μ§λ§μ μμ±λ¨

- μΈμ€ν΄μ€ μ΄λ¦μ μ°Έμ‘°νλ λͺ¨λΈ ν΄λμ€ μ΄λ¦μ λ¨μνμΌλ‘ μμ±νλ κ²μ κΆμ₯

```python
# models.py μμ μμ±
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

λͺ¨λΈμ λν μμ μ¬ν­μ΄ λ°μνκΈ° λλ¬Έμ migration κ³Όμ  μ§ν

```python
python manage.py makemigrations


python manage.py migrate
```

> λͺ¨λΈ νλλ‘ μΈν΄ μμ±λ μ»¬λΌμ μ΄λ¦μ΄ ____.id λ‘ λμ΄
> 
> κ·Έλ κΈ°μ μ°Έμ‘°νλ ν΄λμ€ μ΄λ¦μ μλ¬Έμλ‘ μμ±νλ κ²μ κΆμ₯

`shell_plus μ€ννκΈ° μ μ!`

- pythin pip μ€μΉκ° νμνλ€

```python
$ pip install django-extensions
$ python manage.py shell_plus
```

- μ΄ν μ± μΆκ°κ° νμνλ€.

```python
# settings.py
INSTALLED_APPS = [
    'django_extensions',
]
```

`μνν shell_plus μ€ν`

```python
$ python manage.py shell_plus
```

`λκΈ μμ±`

```python
# Comment ν΄λμ€μ μΈμ€ν΄μ€ comment μμ±
comment = Comment()


# μΈμ€ν΄μ€ λ³μ μ μ₯
comment.content = 'first comment'


# DBμ λκΈ μ μ₯
comment.save()
```

`article = Article.objects.create(title='title',content='content')`

- κ²μκΈ μμ± λ° νμΈ

`article`

`comment.save()`

`comment`

- DBμ λκΈ μ μ₯ λ° νμΈ

`comment.pk`

- pk κ° νμΈ

```python
# 13λ² κ²μκΈμ λͺ¨λ  λκΈμ μκ³ μ νλ€λ©΄?

Comment.objects.filter(aritcle_id=13)
```

```
#Article κ°μ²΄μ λͺ¨λ  λκΈ

aritcle.comment_set.all()
```
