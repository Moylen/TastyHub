from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View

from restaurants.models import RestaurantPlace


class SetBookedOccupied(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    @staticmethod
    def get(request, pk):
        place = RestaurantPlace.objects.get(pk=pk)

        if place.restaurant.admin_user != request.user:
            return redirect('account')

        place.occupied_in = datetime.now().time()
        place.booked_on = None
        place.save()

        return redirect('account')
