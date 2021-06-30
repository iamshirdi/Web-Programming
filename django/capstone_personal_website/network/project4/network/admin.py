from django.contrib import admin
from .models import User,Profile,Certificates,Skills


# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Certificates)
admin.site.register(Skills)