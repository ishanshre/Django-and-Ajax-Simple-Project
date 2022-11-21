from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('profile/', views.UserProfile.as_view(), name='profile'),
    path('profile/', views.profile, name="profile"),
]