from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls.base import reverse_lazy
from .models import Recipes, Category
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormView
from django.views import View
from django.utils.html import strip_tags
from .forms import RecipesCreateForm
from django.urls import reverse

# Create your views here.
class RecipesListView(ListView):
    model = Recipes
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    

class RecipesCreateFormView(FormView):
    form_class = RecipesCreateForm
    template_name = "recipes/recipes_form.html"
    success_url = reverse_lazy('recipes-home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = self.request.user
            form.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})

class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Recipe saved successfully")

class RecipesDetailView(DetailView):
    model = Recipes

class RecipesCreateView(CreateView):
    model = Recipes
    form_class = RecipesCreateForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class}
        return render(request, "recipes/recipes_form.html", context)
    
    def post(self, request, *args, **kwargs):
        form = RecipesCreateForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
            return redirect()