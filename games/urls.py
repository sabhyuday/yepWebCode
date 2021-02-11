from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('feedback/', PostListView.as_view(), name='feedback'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('games/', views.games, name='games'),
    path('games/1/', views.games1, name='games1'),
    path('games/2/', views.games2, name='games2'),
    path('games/3/', views.games3, name='games3'),
    path('games/4/', views.games4, name='games4'),
    path('games/6/', views.games6, name='games6'),

    path('testing/', views.testing, name='testing'),


    

]
