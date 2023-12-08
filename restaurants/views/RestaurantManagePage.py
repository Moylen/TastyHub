from django.shortcuts import redirect, render
from django.views import View

from restaurants.models import Restaurant, RestaurantPlace


class RestaurantManagePage(View):
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
