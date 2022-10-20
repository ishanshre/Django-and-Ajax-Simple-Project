from django.urls import path
from . import views
app_name = 'crud_ajax'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts-data/<int:num_posts>', views.load_post_data_view, name='posts_data'),
    path('like-unlike/', views.likeUnlikePostView, name='like_unlike'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]