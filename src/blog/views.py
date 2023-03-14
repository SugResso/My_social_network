from Tools.scripts.make_ctype import method
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from blog.forms import AddPostForm
from blog.models import Post
from django.contrib.auth.models import User


# Create your views here.

class UserPostListView(ListView):
    # Модель Post из models.py
    model = Post

    # Имя шаблона html
    template_name = 'blog/user_posts.html'

    # object, model_постфикс, наш вариант
    # context - переменная хранения данных
    # представление_модель_что это
    # context_object_name = 'blog_post_user_list'

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-date_created')

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Post.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context['blog_post_user_list'] = queryset.order_by('-date_created')

        return context


def addpost(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-posts-list', request.user.username)
    else:
        form = AddPostForm()
    return render(request, 'blog/form_addpage.html', {'form': form})
