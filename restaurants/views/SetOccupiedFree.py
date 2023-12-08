from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View

from restaurants.models import RestaurantPlace


class SetOccupiedFree(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    @staticmethod
    def get(request, pk):
        place = RestaurantPlace.objects.get(pk=pk)

        if place.user != request.user and place.restaurant.admin_user != request.user:
            return redirect('account')

        place.occupied_in = None
        place.user = None
        place.save()

        return redirect('account')
