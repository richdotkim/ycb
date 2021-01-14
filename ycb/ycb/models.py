from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True)
    prep_time = models.CharField(max_length=30, blank=True)
    cook_time = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    directions = models.TextField()

    def __str__(self):
        return self.title
    

    