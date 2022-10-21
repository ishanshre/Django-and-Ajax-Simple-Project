from django.urls import path
from . import views
app_name = 'crud_ajax'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts-data/<int:num_posts>', views.load_post_data_view, name='posts_data'),
    path('like-unlike/', views.likeUnlikePostView, name='like_unlike'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/data/', views.load_post_detail_data_view, name='post_detail_data'),
    path('<slug:slug>/update/', views.post_detail_udpate, name='post_update'),
    path('<slug:slug>/delete/', views.post_detail_delete, name='post_delete'),
]