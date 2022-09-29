from django.db import models


class Todo(models.Model):
    # django 에서 pk는 자동으로 만들어준다.
    content = models.CharField(max_length=80)
    # default = 데이터를 생성할 떄 값을 안넣으면
    # 자동으로 값을 넣어서 데이터 생성
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    # null = True 를 적용해서 DB 중복입력 과정에서 migrate를 적용 할 수 있다.
