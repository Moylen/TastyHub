from django.shortcuts import render
from django.views import View

from restaurants.models import Restaurant, RestaurantMeal


class RestaurantPage(View):
    @staticmethod
    def get(request, pk):
        restaurant = Restaurant.objects.get(pk=pk)
        meals = RestaurantMeal.objects.filter(restaurant=restaurant)

        context = {
            'restaurant': restaurant,
            'meals': meals
        }
        return render(request, 'restaurants/restaurant_page.html', context)
