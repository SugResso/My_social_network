from django.contrib import admin
from blog.models import Post


# Register your models here.
@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'date_updated', 'author', ]
    prepopulated_fields = {'slug': ('title',)}
