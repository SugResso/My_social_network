# Generated by Django 4.1.6 on 2023-03-13 11:10

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, help_text='до 200 символов', max_length=200, verbose_name='Заголовок')),
                ('content', ckeditor.fields.RichTextField(blank=True, help_text='до 5000 символов', max_length=5000, null=True, verbose_name='Контен')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('likes', models.ManyToManyField(blank=True, related_name='postcomment', to=settings.AUTH_USER_MODEL, verbose_name='Лайки')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_ok', to='blog.post', verbose_name='Репост')),
            ],
            options={
                'verbose_name': 'Создать пост',
                'verbose_name_plural': 'Создать посты',
            },
        ),
    ]
