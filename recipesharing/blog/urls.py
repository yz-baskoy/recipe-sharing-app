from django.urls import path
from . import views
from .views import PostDetail

app_name = 'blog'

urlpatterns = [
    path('sharearecipe/', views.post_view, name='post_view'),
    path('homepage/', views.post_list, name='post_list'),
    path('homepage/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('like/<int:pk>/', views.LikeView, name='like_post'),
]