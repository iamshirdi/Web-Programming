from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>",views.title, name="article"),
    path("search",views.search,name="search"),
    path("add",views.add,name="add"),
    path("wiki/edit/<str:name>",views.edit, name="edit"),
    path ("random",views.rand, name ="random")
]
