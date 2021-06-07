from django.contrib.auth.models import AbstractUser
from django.db import models

#Because it inherits from AbstractUser, it will already have fields for a username, email, password, etc., 
#but you’re welcome to add new fields to the User class if there is additional information about a user that you wish to represent
class User(AbstractUser):
    pass

#wbt user comments list
class comments(models.Model):
    comment = models.CharField(max_length=256)
    comment_user = models.CharField(max_length=256)
    comment_date = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.comment}, {self.comment_date}"

class bid(models.Model):
    bid_price = models.DecimalField(max_digits=5, decimal_places=2)
    bid_user = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.bid_price, self.bid_user}"

class Categorys(models.Model):
    cat = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.cat}"

class list_status(models.Model):
    name = models.CharField(max_length=64)

class watch_list(models.Model):
    #need to add duplicate article id error checking in future 
    article_id = models.IntegerField()
    user_id = models.IntegerField()
    

class auction(models.Model):
    title = models.CharField(max_length=64)
    url = models.CharField(max_length=64,blank=True)
    description = models.CharField(max_length=128)
    comment = models.ManyToManyField(comments, related_name="all_comments",blank=True)
    category = models.ManyToManyField(Categorys, related_name="categories")
    price = models.ForeignKey(bid, on_delete=models.CASCADE, related_name="bids_filter")
    created_date = models.DateField(auto_now=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_filter")
    status = models.ForeignKey(list_status, on_delete=models.CASCADE, related_name="status_filter")
    

    def __str__(self):
        return f"{self.title}: {self.category}, {self.description}"


