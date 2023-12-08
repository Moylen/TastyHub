from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from restaurants.models import Restaurant, RestaurantPlace
from users.forms import UserEditForm


class ProfilePage(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    @staticmethod
    def get(request):
        # Если аккаунт ресторана
        restaurant = Restaurant.objects.filter(admin_user=request.user)
        if restaurant:
            return redirect('manage')

        user_places = RestaurantPlace.objects.filter(user=request.user).order_by('booked_on')

        context = {
            'user_places': user_places,
            'UserEditForm': UserEditForm(instance=request.user)
        }
        return render(request, 'restaurants/profile_page.html', context)

    @staticmethod
    def post(request):
        form = UserEditForm(request.POST, instance=request.user)
        if not form.is_valid():
            return render(request, 'restaurants/profile_page.html', {'UserEditForm': form})

        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        if password:
            user.set_password(password)
        user.save()

        updated_user = authenticate(username=user.username, password=password)
        if updated_user is not None:
            login(request, updated_user)

        return redirect('account')
