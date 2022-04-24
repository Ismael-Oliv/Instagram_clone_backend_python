import uuid
from django.db import models


class Post(models.Model):
    tb_name = "post"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey("user.User", on_delete=models.CASCADE)
    comments_id = models.ForeignKey("comment.Comments", on_delete=models.CASCADE)
    likes_id = models.ForeignKey("like.Likes", on_delete=models.CASCADE)
    content_1 = models.CharField(max_length=50, null=False)
    content_2 = models.CharField(max_length=50, null=True)
    content_3 = models.CharField(max_length=50, null=True)
    content_4 = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
