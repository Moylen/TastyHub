from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from restaurants.models import Restaurant, RestaurantPlace


class RestaurantManagePage(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    @staticmethod
    def get(request):
        restaurant = Restaurant.objects.get(admin_user=request.user)

        # Если пользователь не администратор ресторана
        if not restaurant:
            return redirect('index')

        restaurant_places = RestaurantPlace.objects.filter(restaurant=restaurant)

        context = {
            'restaurant_places': restaurant_places,
            'restaurant': restaurant
        }
        return render(request, 'restaurants/restaurant_manage_page.html', context)

    @staticmethod
    def post(request):
        return redirect('index')
