from  django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.utils.translation import gettext_lazy as _

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(label=_('Profile Picture'),required=False, error_messages = {'invalid':_("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ['image']