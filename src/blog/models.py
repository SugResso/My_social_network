from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    title = models.CharField(max_length=200, help_text='до 200 символов', db_index=True, verbose_name='Заголовок')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    content = RichTextField(max_length=5000, blank=True, null=True, help_text='до 5000 символов', verbose_name='Контен')
    date_created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор(ша)')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')
    likes = models.ManyToManyField(User, related_name='postcomment', blank=True, verbose_name='Лайки')
    reply = models.ForeignKey('self', blank=True, null=True, related_name='reply_ok', on_delete=models.CASCADE, verbose_name='Репост')

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
