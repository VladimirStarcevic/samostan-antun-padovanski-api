from django.urls import path
from .views import PostListAPIView

app_name = 'blog'

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post_list_api')

]