# accounts/forms.py 생성후 아래와 같이 채움

'''
URL-VIEW-TEMPLATE 단계로 넘어가기 전에, 
UserCreationForm() 커스텀하는 단계
'''

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': '닉네임',
            'email' : '이메일',
            'password1': '비밀번호',
            'password2': '비밀번호 확인'
    }