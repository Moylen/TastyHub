from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import View

from restaurants.forms import BookingForm
from restaurants.models import RestaurantPlace


class Reserve(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    @staticmethod
    def post(request, pk):
        form = BookingForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest('Form is not valid')

        place = RestaurantPlace.objects.get(pk=pk)

        # Если место уже забронировано или занято
        if place.booked_on or place.occupied_in:
            messages.error(request, 'Место забронировано или занято.')
            return redirect(reverse('booking', kwargs={'pk': place.restaurant_id}))

        # Если пользователь уже забронировал один стол в этом ресторане
        if RestaurantPlace.objects.filter(user=request.user, restaurant=place.restaurant):
            messages.error(request, 'Место в ресторане уже забронировано.')
            return redirect(reverse('booking', kwargs={'pk': place.restaurant_id}))

        # Если пользователь выбрал время для брони меньше текущего
        current_time = timezone.localtime(timezone.now()).time()
        if form.cleaned_data['booked_on'] < current_time:
            messages.error(request, 'Время бронирования заполнено неверно.')
            return redirect(reverse('booking', kwargs={'pk': place.restaurant_id}))

        # Если все проверки пройдены
        place.booked_on = form.cleaned_data['booked_on']
        place.user = request.user
        place.save()

        return redirect('account')
