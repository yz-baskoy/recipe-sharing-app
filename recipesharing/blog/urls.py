from django.urls import path
from . import views
from .views import PostDetail, CreateNewPost

app_name = 'blog'

urlpatterns = [
    path('sharearecipe/', CreateNewPost.as_view(), name='post_view'),
    path('homepage/', views.post_list, name='post_list'),
    path('homepage/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('like/<int:pk>/', views.LikeView, name='like_post'),
    path('rate/<int:pk>/',views.rate_view, name='rate_post'),
]

 