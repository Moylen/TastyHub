from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from restaurants.models import Restaurant, RestaurantPlace
from users.forms import UserEditForm, UserPassForm


class AccountPage(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    @staticmethod
    def get(request):
        # Если аккаунт ресторана
        restaurant = Restaurant.objects.filter(admin_user=request.user)
        if restaurant:
            return redirect('manage')

        user_places = RestaurantPlace.objects.filter(user=request.user).exclude(booked_on=None).order_by('booked_on')

        context = {
            'user_places': user_places,
            'UserEditForm': UserEditForm(instance=request.user),
            'UserPassForm': UserPassForm(instance=request.user)
        }
        return render(request, 'restaurants/account_page.html', context)

    @staticmethod
    def post(request):

        if 'UserEditForm' in request.POST:
            edit_form = UserEditForm(request.POST, instance=request.user)
            if edit_form.is_valid():
                edit_form.save(commit=True)
                return redirect('account')
            else:
                context = {
                    'UserEditForm': edit_form,
                    'UserPassForm': UserPassForm()
                }
                return render(request, 'restaurants/account_page.html', context)

        if 'UserPassForm' in request.POST:
            pass_form = UserPassForm(request.POST, instance=request.user)
            if pass_form.is_valid():
                user = pass_form.save(commit=False)
                password = pass_form.cleaned_data.get('password')
                user.set_password(password)
                user.save()
                return redirect('account')
            else:
                context = {
                    'UserEditForm': UserEditForm(instance=request.user),
                    'UserPassForm': pass_form
                }
                return render(request, 'restaurants/account_page.html', context)

        return redirect('account')
