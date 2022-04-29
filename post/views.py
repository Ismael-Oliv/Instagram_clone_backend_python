from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


@api_view(["GET"])
def get_posts_controller(request, *args, **kwargs):
    posts = []
    posts_query = Post.objects.all()
    if posts_query:
        posts = PostSerializer(posts_query, many=True)

    return Response(status=200, data=posts)


@api_view(["GET"])
def get_post_controller(request, *args, **kwargs):
    posts = []
    id = request.query_params["id"]
    posts_query = Post.objects.get(ic=id)
    if posts_query:
        posts = PostSerializer(posts_query, many=True)
        return Response(status=200, data=posts)

    return Response(status=404)


@api_view(["POST"])
def create_post_controller(request, *args, **kwargs):
    post_data = {
        "user_id": request.data["user_id"],
        "content_id": request.data["content_id"]
    }

    posts_serialized = PostSerializer(data=post_data)
    post = {}
    if posts_serialized.is_valid(raise_exception=True):
        posts_serialized.save()

        post = posts_serialized.data

    return Response(status=201, data=post)


@api_view(["DELETE"])
def delete_post_controller(request, *args, **kwargs):
    post_query = Post.objects.get(ic="id")

    if post_query:
        post_query.delete()
        return Response(status=202)

    return Response(status=404)
