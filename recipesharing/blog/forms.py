from django import forms
from .models import *

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'image', 'description', 'difficulty', 'select_ingredients']

        widgets = {
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['score']