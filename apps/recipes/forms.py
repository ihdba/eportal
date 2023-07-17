from django import forms
from django.forms import ModelForm

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        #fields = '__all__'
        fields = ['name', 'recipe', 'image']