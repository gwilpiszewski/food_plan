from django.db import models


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=128)
    ingredients = models.TextField(max_length=500)
    description = models.TextField(max_length=1200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    preparation_time = models.DurationField()
    votes = models.SmallIntegerField()

