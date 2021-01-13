from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib import messages

def home(request):
    return render (request, 'ycb/home.html')

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
            return render(request, 'accounts/login.html', context)


    context = {}
    return render (request, 'ycb/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')