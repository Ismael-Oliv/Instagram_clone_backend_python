from django.db import models
import uuid


class Comments(models.Model):
    db_table = "comments"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey("user.User", on_delete=models.CASCADE)
    post_id = models.ForeignKey("post.Post", on_delete=models.CASCADE)
    comments = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
