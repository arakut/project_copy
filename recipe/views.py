from django.http import HttpResponse
from django.shortcuts import render
from recipe.models import Recipe, Food
from django.views.generic import ListView, DetailView
from recipe.models import Recipe, Food
from recipe.forms import FoodForm


class ListObjectsView1(ListView):
    model = Food
    template_name = 'action1.html'
    context_object_name = 'food'

    def post(self, request, *args):
        return Food.objects.all()


class ListObjectsView2(ListView):
    model = Food
    template_name = 'action2.html'
    context_object_name = 'food'


# def click_view_one(request):
#     form = {}
#     food = Food.objects.all()
#     form['food'] = food
#     print(food)
#     if request.method == 'POST':
#         click = True if request.POST.get('click') else False
#         title = request.POST.get('title', False)
#         form['title'] = title
#         return render(request, 'action2.html', form)
#     return render(request, 'action1.html', {'form': FoodForm})


def click_view_two(request):
    pass


class DetailObjectsView(DetailView):
    model = Recipe
    template_name = 'recipe.html'
    context_object_name = 'recipe'
