import uuid
from django.db import models


class User(models.Model):
    db_table = "user"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, null=False, unique=True)
    email = models.CharField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=50, null=False)
    avatar_url = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
