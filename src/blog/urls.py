from django.urls import path, re_path

from blog.views import UserPostListView, addpost


urlpatterns = [
    path('posts/user/<str:username>/', UserPostListView.as_view(), name='user-posts-list'),
    path('register/', addpost, name='add_page'),
]