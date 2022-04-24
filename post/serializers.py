from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "user_id",
            "content_1",
            "content_2",
            "content_3",
            "content_4",
            "created_at"
        ]
