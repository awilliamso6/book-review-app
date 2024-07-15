from django.contrib import admin
from .models import Profile, Book, Thought

# Register your models here.
admin.site.register([Profile, Book, Thought])