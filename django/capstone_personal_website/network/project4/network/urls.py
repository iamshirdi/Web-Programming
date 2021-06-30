
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/<str:name>", views.profile, name="profile"),
    path("add_entity", views.add_entity, name="add_entity"),
    path("add_skills", views.add_skills, name="add_skills"),
    path("del_entity", views.del_entity, name="del_entity"),
    path("profile/<str:name>/projects", views.projects, name="projects"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
