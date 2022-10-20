from django import forms
from .models import Article,Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'title': '제목',
            'content' : '내용',
            'image' : '이미지',
            'thumbnail' : '썸네일'
    }

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment 
#         fields = ['content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "여러분의 댓글을 기다리고 있어요!",
        })
    )
    class Meta:
        model = Comment 
        fields = ['content']