from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer


@api_view(["POST"])
def add_comment_controller(request, *args, **kwargs):
    comment_data = {
        "user_id": request.data["user_id"],
        "content_id": request.data["content_id"]
    }

    comment_serialized = CommentSerializer(data=comment_data)
    comment = {}
    if comment_serialized.is_valid(raise_exception=True):
        comment_serialized.save()

        comment = comment_serialized.data

    return Response(status=201, data=comment)
