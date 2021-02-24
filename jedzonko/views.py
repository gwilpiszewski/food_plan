from datetime import datetime
from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from django.views import View
from jedzonko.models import Recipe, Plan
import random


class IndexView(View):

    def get(self, request):
        recipes = Recipe.objects.all()
        recipes = [x for x in recipes]
        random.shuffle(recipes)
        recipes = recipes[:3]
        ctx = {"actual_date": datetime.now(), "recipes": recipes}
        return render(request, "index.html", ctx)


class RecipeListView(View):

    def get(self, request):
        list_of_recipes = Recipe.objects.all().order_by('-created').order_by('-votes')

        paginator = Paginator(list_of_recipes, 2)  # tu ustawia się ile elementów ma pojawiać się na stronie, do testów 1 (powinno być 50)
        page = request.GET.get('page')
        recipes = paginator.get_page(page)
        list_of_pagenumbers = [i for i in range(1, recipes.paginator.num_pages + 1)]  # lista do interowania w for do środkowej części paginatora

        ctx = {'recipes': recipes, 'list_of_pagenumbers': list_of_pagenumbers}
        return render(request, 'app-recipes.html', ctx)


class DashboardView(View):

    def get(self, request):
        number_of_plans = Plan.objects.all().count()
        number_of_recipes = Recipe.objects.all().count()
        context = {"number_of_plans": number_of_plans, "number_of_recipes": number_of_recipes}
        return render(request, "dashboard.html", context=context)


class PlanListView(View):

    def get(self, request):
        list_of_plans = Plan.objects.all().order_by('name')

        paginator = Paginator(list_of_plans, 2)
        page = request.GET.get('page')
        plans = paginator.get_page(page)
        list_of_pagenumbers = [i for i in range(1, plans.paginator.num_pages + 1)]

        context = {'plans': plans, 'list_of_pagenumbers': list_of_pagenumbers}
        return render(request, "app-schedules.html", context=context)


class RecipeAddView(View):

    def get(self, request):
        message = ""
        context = {'message': message}
        return render(request, "app-add-recipe.html", context=context)

    def post(self, request):

        name = request.POST['name']
        description = request.POST['description']
        preparation_time = request.POST['preparation_time']
        preparation_method = request.POST['preparation_method']
        ingredients = request.POST['ingredients']

        if (name != '' and description != '' and preparation_time != ''
                and preparation_method != '' and ingredients != ''):
            Recipe.objects.create(
                name=name,
                description=description,
                preparation_time=preparation_time,
                preparation_method=preparation_method,
                ingredients=ingredients
            )
            return redirect('/recipe/list')
        else:
            return render(request, "app-add-recipe.html", context={"message": "Wypełnij poprawnie wszystkie pola"})


class PlanAddView(View):

    def get(self, request):
        return render(request, "tu bedzie html plan add")


class PlanAddRecipeView(View):

    def get(self, request):
        return render(request, "tu bedzie html plan add recipe")


class AboutView(View):

    def get(self, request):
        return render(request, 'index.html')


class ContactView(View):

    def get(self, request):
        return render(request, 'index.html')


class RecipeView(View):

    def get(self, requst):
        return render(requst, "tu będzie html recipe id")
