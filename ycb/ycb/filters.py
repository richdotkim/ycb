import django_filters
from django_filters import CharFilter

from .models import Recipe

class RecipeFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='')
    class Meta:
        model = Recipe
        fields = ['title']
