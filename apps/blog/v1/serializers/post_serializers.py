from rest_framework import serializers
from apps.blog.models import Post

class PostInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()


class PostOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

