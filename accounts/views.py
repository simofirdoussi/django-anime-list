from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def registration_view(response):

    form = RegisterForm()
    if response.method=="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(response, user)
            return redirect('home')

    context = {
        'form': form
    }

    return render(response, 'accounts/register.html', context)

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
