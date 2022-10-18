from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/',blank=True)
    thumbnail = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality':90},
    )

def __str__(self):
    return self.title


class Comment(models.Model):
    content = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


