from datetime import datetime

from django.shortcuts import render
from django.views import View
from jedzonko.models import Recipe


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "index.html", ctx)


class RecipeListView(View):

    def get(self, request):
        list_of_recipes = Recipe.objects.all()
        ctx = {'list_of_recipes': list_of_recipes}
        return render(request, 'app-recipes.html', ctx)


class DashboardView(View):

    def get(self, request):
        number_of_plans = 0  # Plan.objects.all().count()  # po dodaniu modelu 'Plan' odkomentować
        number_of_recipes = Recipe.objects.all().count()
        context = {"number_of_plans": number_of_plans, "number_of_recipes": number_of_recipes}
        return render(request, "dashboard.html", context=context)


class PlanListView(View):

    def get(self, request):
        return render(request, "tu bedzie html plan list")


class RecipeAddView(View):

    def get(self, request):
        return render(request, "tu bedzie html recipe add")


class PlanAddView(View):

    def get(self, request):
        return render(request, "tu bedzie html plan add")


class PlanAddRecipeView(View):

    def get(self, request):
        return render(request, "tu bedzie html plan add recipe")
