from datetime import datetime

from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}

        return render(request, "index.html", ctx)


class DashboardView(View):

    def get(self, request):

        return render(request, "dashboard.html")


class RecipeListView(View):

    def get(self, request):

        return render(request, "tu bedzie html recipe list")


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