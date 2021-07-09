from users.forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
from .models import Profile
from recipes.models import Recipes
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect

# Create your views here.
@login_required
def profile(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, 'Your profile has been updated')
            return redirect('users-profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = u_form = UserUpdateForm(instance=request.user)
    context = {'p_form': p_form, 'u_form': u_form}
    return render(request, "users/profile.html", context)

@login_required
def favourite_list(request):
    fav_list = Recipes.objects.filter(favourites=request.user)
    return render(request, 'account/favourites.html', {'fav_list': fav_list})

@login_required
def favourite_add(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    if recipe.favourites.filter(pk=request.user.id).exists():
        recipe.favourites.remove(request.user)
    else:
        recipe.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

