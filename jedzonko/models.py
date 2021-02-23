from django.db import models


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=128)
    ingredients = models.TextField(max_length=500)
    description = models.TextField(max_length=1200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    preparation_time = models.SmallIntegerField(default=0)
    votes = models.SmallIntegerField(default=0)

class Plan(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=1200)
    created = models.DateTimeField(auto_now_add=True)
    recipes = models.ManyToManyField(Recipe, through="RecipePlan")

class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=32)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order = models.