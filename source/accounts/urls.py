from django.urls import path

from accounts import views
from accounts.views import logout_view, ProfileView, UserChangeView, CreatePost, like_post

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change', UserChangeView.as_view(), name='change'),
    path('create/', CreatePost.as_view(), name='create_post'),
    path('<int:post_id>/like_post/', like_post, name='like_post'),
]