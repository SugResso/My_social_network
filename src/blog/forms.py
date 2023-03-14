from django import forms
from .models import *
from ckeditor.fields import RichTextField


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # текст в поле, если оно пустое
        self.fields['author'].empty_label = 'Не выбран(а)'

    class Meta:
        # связываем форму с моделью, чтобы она понимала
        model = Post
        #
        fields = ('title', 'photo', 'content', 'author', 'slug')

        #
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
