
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("profile/<str:name>", views.profile_view, name="profile"),
    path("follow/<str:name>", views.follow_view, name="follow_view"),
    path("following", views.following_view, name="following_view"),
    path("edit_post", views.edit_post, name="edit_post"),
    path("edit_like", views.edit_like, name="edit_like"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
