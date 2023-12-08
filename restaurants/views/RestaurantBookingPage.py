from datetime import datetime, timedelta

from django.shortcuts import render
from django.utils import timezone
from django.views import View

from restaurants.forms import BookingForm
from restaurants.models import Restaurant, RestaurantPlace


class RestaurantBookingPage(View):
    @staticmethod
    def get(request, pk):
        restaurant = Restaurant.objects.get(pk=pk)
        restaurant_places = RestaurantPlace.objects.filter(restaurant=restaurant)

        # Если место не заняли за timedelta, то бронирование обнуляется
        current_time = timezone.localtime(timezone.now()).time()
        for place in restaurant_places:
            if place.booked_on is None:
                continue
            expired_place_time = (datetime.combine(datetime.today(), place.booked_on) + timedelta(minutes=15)).time()
            if expired_place_time < current_time:
                place.booked_on = None
                place.user = None
                place.save()

        restaurant_places = RestaurantPlace.objects.filter(restaurant=restaurant)

        context = {
            'restaurant_places': restaurant_places,
            'restaurant': restaurant,
            'BookingForm': BookingForm()
        }
        return render(request, 'restaurants/booking_page.html', context)
