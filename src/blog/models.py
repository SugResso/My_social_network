from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать пост'

    title = models.CharField(max_length=200, help_text='до 200 символов')
    content = models.TextField(max_length=5000, blank=True, null=True, help_text='до 5000 символов')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title