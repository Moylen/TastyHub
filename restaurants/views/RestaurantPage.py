from django.shortcuts import render
from django.views import View

from restaurants.models import Restaurant


class RestaurantPage(View):
    @staticmethod
    def get(request, pk):
        restaurant = Restaurant.objects.get(pk=pk)
        return render(request, 'restaurants/restaurant_page.html', {'restaurant': restaurant})