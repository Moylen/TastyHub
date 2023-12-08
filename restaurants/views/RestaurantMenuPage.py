from django.shortcuts import render
from django.views import View


class RestaurantMenuPage(View):
    @staticmethod
    def get(request, pk):
        return render(request, 'restaurants/restaurant_menu_page.html')
