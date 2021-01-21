from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, AddRecipeForm

from django.contrib import messages
from .models import Recipe
from .filters import RecipeFilter

def home(request):
    recipes = Recipe.objects.all()

    myFilter = RecipeFilter(request.GET, queryset=recipes)
    recipes = myFilter.qs

    context = {'recipes':recipes, 'myFilter':myFilter}
    return render (request, 'ycb/home.html', context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account for ' + user + ' was created successfully!')
            return redirect('login')

    context = {'form': form}
    return render (request, 'ycb/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render (request, 'ycb/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    queryset = Recipe.objects.all()

    context = {'recipe': recipe, 'queryset':queryset}
    return render(request, 'ycb/recipe.html', context)

def addRecipe(request):
    form = AddRecipeForm()

    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'ycb/add_recipe.html', context)