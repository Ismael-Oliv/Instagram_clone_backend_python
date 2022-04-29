from django.db import models
import uuid


class Likes(models.Model):
    db_table = "likes"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey("user.User", on_delete=models.CASCADE)
    post_id = models.ForeignKey("post.Post", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
