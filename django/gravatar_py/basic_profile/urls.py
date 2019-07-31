from . import views
from django.urls import path
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('json/', views.userJson, name='gravatarProfileData'),
    path('', views.user, name='userProfile'),
]
