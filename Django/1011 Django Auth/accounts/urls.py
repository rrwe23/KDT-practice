# accounts/urls.py 에 아래와 같이 path 추가
# 추가된 코드 : path('<int:pk>/', views.detail, name='detail'),

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
]