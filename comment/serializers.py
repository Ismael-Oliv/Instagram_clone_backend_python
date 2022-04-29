from rest_framework import serializers
from .models import Comments


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            "id",
            "user_id",
            "post_id",
            "content",
            "created_at",
            "updated_at"
        ]