from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.get_posts_controller),
    path("one/:id", views.get_post_controller),
    path("create/", views.create_post_controller),
    path("delete/:id", views.delete_post_controller),

]