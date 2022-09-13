from django.db import models


class Food(models.Model):
    image = models.ImageField(upload_to='static/posts')
    title = models.CharField(max_length=50, null=True, blank=True)
    click = models.BooleanField

    def __str__(self):
        return f'Title:{self.title}'


class Recipe(models.Model):
    image = models.ImageField(upload_to='static/posts')
    title = models.CharField(max_length=50, null=True, blank=True)
    ingredients = models.TextField(max_length=500)
    description = models.TextField(max_length=3000)
    # rec = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title:{self.title}'
