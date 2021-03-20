from django import forms
from .models import *

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'image', 'description', 'difficulty', 'select_ingredients']

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control', 'value': '', 'id':'formid'}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows':5, 'col':70, 'class': 'form-control'}),
        }

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['score']