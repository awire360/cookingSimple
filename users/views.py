from users.forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

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