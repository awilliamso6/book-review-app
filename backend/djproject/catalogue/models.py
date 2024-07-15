from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)


class Book(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    display_title = models.CharField(max_length=200)


class Thought(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page_num = models.IntegerField("Page Number")
    text = models.CharField("Thoughts", max_length=500)
