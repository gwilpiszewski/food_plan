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

class Dayname(models.Model):
    day_names = (
        (1, "Poniedziałek"),
        (2, "Wtorek"),
        (3, "Środa"),
        (4, "Czwartek"),
        (5, "Piątek"),
        (6, "Sobota"),
        (7, "Niedziela"),
        )
    day = models.IntegerField(choices=day_names, null=True)

class RecipePlan(models.Model):
    meal_names = (
        (1, "Śniadanie"),
        (2, "Drugie śniadanie"),
        (3, "Obiad"),
        (4, "Podwieczorek"),
        (5, "Kolacja"),
    )
    meal_names = models.IntegerField(choices=meal_names)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order = models.IntegerField(choices=meal_names, null=True)
    day_name = models.ForeignKey(Dayname, on_delete=models.CASCADE)