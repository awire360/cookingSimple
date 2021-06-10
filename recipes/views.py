from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipes
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormView
from django.views import View
from django.utils.html import strip_tags
from .forms import RecipesCreateForm

# Create your views here.
class RecipesListView(ListView):
    model = Recipes

class RecipesCreateFormView(FormView):
    form_class = RecipesCreateForm
    template_name = "recipes/recipes_form.html"
    success_url = '/recipes/success'

    
    def get_context_data(self, **kwargs):
        context = super(RecipesCreateForm, self).get_context_data(**kwargs)
        context['cookingsteps'] = 
        return context
    

    def form_valid(self, form) -> HttpResponse:

        form.save()
        return super().form_valid(form)

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