from unittest.util import _MAX_LENGTH
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()
    running_time = models.IntegerField()

