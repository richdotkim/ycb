from django.db import models

class Recipe(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='title')
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    prep_time = models.CharField(max_length=30, blank=True)
    cook_time = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    directions = models.TextField(blank=True)

    def __str__(self):
        return self.title
    

    