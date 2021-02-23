from datetime import datetime
from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from django.views import View
from jedzonko.models import Recipe


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "index.html", ctx)


class RecipeListView(View):

    def get(self, request):
        list_of_recipes = Recipe.objects.all().order_by('-created').order_by('-votes')

        paginator = Paginator(list_of_recipes, 2) #tu ustawia się ile elementów ma pojawiać się na stronie, do testów 1 (powinno być 50)
        page = request.GET.get('page')
        recipes = paginator.get_page(page)
        list_of_pagenumbers = [i for i in range(1, recipes.paginator.num_pages+1)] #lista do interowania w for do środkowej części paginatora

        ctx = {'recipes': recipes, 'list_of_pagenumbers': list_of_pagenumbers}
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
        return render(request, "app-add-recipe.html")

    def post(self, request):
        name = request.POST['name']
        description = request.POST['description']
        preparation_time = request.POST['preparation_time']
        preparation_method = request.POST['preparation_method']
        ingredients = request.POST['ingredients']
        Recipe.objects.create(
            name=name,
            description=description,
            preparation_time=preparation_time,
            preparation_method=preparation_method,
            ingredients=ingredients
        )
        return redirect('/')  # tymczasowe


class PlanAddView(View):

    def get(self, request):
        return render(request, "tu bedzie html plan add")


class PlanAddRecipeView(View):

    def get(self, request):
        return render(request, "tu bedzie html plan add recipe")
