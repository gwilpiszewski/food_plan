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
        # template = f"""
        #             <tr class="d-flex">
        #             <th scope="row" class="col-1">1</th>
        #             <td class="col-2">
        #                 {{ recipes_title }}
        #             </td>
        #             <td class="col-7"> {{ recipes_content}}
        #             </td>
        #             <td class="col-2 d-flex align-items-center justify-content-center flex-wrap">
        #                 <a href="#"
        #                    class="btn btn-danger rounded-0 text-light m-1">Usuń</a>
        #                 <a href="/app-recipe-details.html"
        #                    class="btn btn-info rounded-0 text-light m-1">Szczegóły</a>
        #                 <a href="/app-edit-recipe.html"
        #                    class="btn btn-warning rounded-0 text-light m-1">Edytuj</a>
        #             </td>
        #             </tr>
        # """

        myrange = [1, 2, 3, 4, 5, 6]
        ctx = {'myrange': myrange}
        # ctx = {'template': template}
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
