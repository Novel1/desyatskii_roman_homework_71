from rest_framework import serializers

from posts.models import Post, Like


class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'descriptions']


