from typing import Any, Dict
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls.base import reverse_lazy
from .models import Recipe, Category
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormView
from django.views import View
from django.utils.html import strip_tags
from .forms import RecipeCreateForm
from django.urls import reverse

# Create your views here.
# class RecipeListView(ListView):
#     model = Recipe
#     paginate_by = 20
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["categories"] = Category.objects.all()
#         context['fav'] = Recipe.objects.filter()
#         return context

def recipeListView(request):
    recipes = Recipe.objects.all().select_related('category')
    context = {
        'recipes': recipes,
    }
    if request.htmx:
        return render(request, "recipes/recipe_list_partial.html", context)
    return render(request, "recipes/recipe_list.html", context)

class MyRecipeListView(ListView):
    model = Recipe
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user).order_by('-updated_at')

def recipeCreateForm(request):
    if request.method == "POST":
        form = RecipeCreateForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipes-home')
    else:
        form = RecipeCreateForm()
    return render(request, "recipes/recipe_form.html", {'form': form})

class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Recipe saved successfully")

# class RecipesDetailView(DetailView):
#     model = Recipes
#     fav = bool
#     context = dict
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['fav'] = self.fav
#         return context

#     def get(self, request, *args, **kwargs) -> HttpResponse:
#         recipe = get_object_or_404(Recipes, id=request.pk)
#         if recipe.favourites.filter(pk=request.user.id).exists():
#             self.fav = True
#         return render(request, "recipes/recipes_detail.html", self.context)
def recipeDetailView(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    fav = bool
    if recipe.favourites.filter(pk=request.user.id).exists():
        fav = True
    context = {
        'recipe': recipe,
        'fav': fav
    }
    return render(request, "recipe/recipe_detail.html", context)

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class}
        return render(request, "recipe/recipe_form.html", context)
    
    def post(self, request, *args, **kwargs):
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
            return redirect()

@login_required
def favourite_add(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.favourites.filter(pk=request.user.id).exists():
        recipe.favourites.remove(request.user)
    else:
        recipe.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])