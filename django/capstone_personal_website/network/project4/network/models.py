from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Profile(models.Model):
    profile_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_user")
    entity = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date =  models.DateField()
    entity_desc = models.CharField(max_length=2560)
    entity_type =models.CharField(max_length=2560)
# education, job, project

class Skills(models.Model):
    profile_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills_user")
    skills = models.CharField(max_length=2560)

class Certificates(models.Model):
    profile_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certificates_user")
    certificates = models.CharField(max_length=2560)
