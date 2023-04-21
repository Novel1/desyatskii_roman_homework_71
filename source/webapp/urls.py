from django.urls import path

from webapp.views import search_users, IndexView, CommentView, PostDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', search_users, name='search_users'),
    path('comment/<int:pk>/', CommentView.as_view(), name='comment'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]