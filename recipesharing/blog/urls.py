from django.urls import path
from . import views
from .views import PostDetail, CreateNewPost, PostList, SearchView, UpdatePostView

app_name = 'blog'

urlpatterns = [
    path('sharearecipe/', CreateNewPost.as_view(), name='post_view'),
    path('edit/<int:pk>', UpdatePostView.as_view(), name='edit_view' ),
    path('homepage/', PostList.as_view(), name='post_list'),
    path('homepage/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('like/<int:pk>/', views.like_view, name='like_post'),
    path('rate/<int:pk>/',views.rate_view, name='rate_post'),
    path('search', SearchView.as_view(), name='search'),
]

 