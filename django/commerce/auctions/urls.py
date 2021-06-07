from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("watch", views.watch, name="watch"),
    path("bid", views.b_id, name="bid"),
    path("close", views.close, name="close"),
    path("com", views.com, name="com"),
    path("delid", views.del_watch, name="delid"),
    path("<int:list_id>/details",views.detail, name="details"),
    path("category",views.cat,name="cat")
]
