from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, logout

# Create your views here.


class UserRegistrationPage(View):
    @staticmethod
    def get(request):
        return render(request, 'users/registration.html', {'form': UserRegistrationForm()})
    
    @staticmethod
    def post(request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'users/registration.html', {'form': form})
    

class UserLoginPage(View):
    @staticmethod
    def get(request):
        return render(request, 'users/login.html', {'form': UserLoginForm()})
    
    @staticmethod
    def post(request):
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        return render(request, 'users/login.html', {'form': form})
    

class UserLogoutView(View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect('login')
