from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers import PostSerializers
from posts.models import Post


# Create your views here.

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        elif self.action in ['create', 'like', 'unlike', 'destroy']:
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        else:
            return [AllowAny()]




