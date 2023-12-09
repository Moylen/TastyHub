from django.shortcuts import redirect
from django.views import View

from restaurants.models import RestaurantPlace


class SetAllFree(View):
    @staticmethod
    def get(request, pk):
        RestaurantPlace.objects.filter(restaurant_id=pk).update(booked_on=None, occupied_in=None, user=None)
        return redirect('account')
