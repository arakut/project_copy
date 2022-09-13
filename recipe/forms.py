from django import forms
from recipe.models import Food


class FoodForm(forms.Form):
    class Meta:
        model = Food


# class FoodForm(forms.Form):
#     image = forms.ImageField()
#     title = forms.CharField(max_length=50)
#     click = forms.BooleanField
