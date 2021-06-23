from django.contrib import admin
from .models import User, Posts ,follow_db

# Register your models here.
admin.site.register(User)
admin.site.register(Posts)
admin.site.register(follow_db)