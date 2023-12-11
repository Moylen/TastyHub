from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View

from restaurants.models import RestaurantPlace


class SetAllFree(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    @staticmethod
    def get(request, pk):
        places = RestaurantPlace.objects.filter(restaurant_id=pk)

        if places[0].restaurant.admin_user != request.user:
            return redirect('account')

        places.update(booked_on=None, occupied_in=None, user=None)

        return redirect('account')
