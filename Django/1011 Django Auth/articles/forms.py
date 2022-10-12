# ModelForm 생성하기
# articles/forms.py 파일 새로 생성해서 아래와 같이 코드 채우기
# Article model 에 있는 모든 fields 를 가져다가 쓰겠다는 의미임

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

# 만약 여기서 title 입력란만 생성하고 싶으면
# Meta class 안에 fields = ['title'] 이렇게 작성하면 되고,
# title, content 입력란 생성하고 싶으면
# Meta class 안에 fields = ['title', 'content'] 이렇게 작성