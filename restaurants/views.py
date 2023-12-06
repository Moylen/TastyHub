from datetime import timedelta, datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import View

from users.forms import UserEditForm
from .forms import FilterForm, BookingForm
from .models import Restaurant, RestaurantPlace
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class Index(View):
    @staticmethod
    def get(request):
        restaurants = Restaurant.objects.all()

        context = {'FilterForm': FilterForm(), 'restaurants': restaurants}
        return render(request, 'restaurants/index.html', context)

    @staticmethod
    def post(request):
        form = FilterForm(request.POST)
        if not form.is_valid():
            return render(request, 'restaurants/index.html', {'FilterForm': form})

        kitchen_type = form.cleaned_data['name']
        restaurants = Restaurant.objects.filter(kitchen_type=kitchen_type)

        context = {'FilterForm': form, 'restaurants': restaurants}
        return render(request, 'restaurants/index.html', context)


class RestaurantPage(View):
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
            'BookingForm': BookingForm()
        }
        return render(request, 'restaurants/booking_page.html', context)


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
            return HttpResponseBadRequest('Place already booked or occupied')

        # Если пользователь уже забронировал один стол в этом ресторане
        if RestaurantPlace.objects.filter(user=request.user, restaurant=place.restaurant):
            return HttpResponseBadRequest('User already booked place in this restaurant')

        # Если пользователь выбрал время для брони меньше текущего
        current_time = timezone.localtime(timezone.now()).time()
        if form.cleaned_data['booked_on'] < current_time:
            return HttpResponseBadRequest('Cannot book place in this time')

        # Если все проверки пройдены
        place.booked_on = form.cleaned_data['booked_on']
        place.user = request.user
        place.save()

        return redirect('profile')


class ReserveDelete(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    @staticmethod
    def get(request, pk):
        place = RestaurantPlace.objects.get(pk=pk)

        if place.user != request.user:
            return redirect('profile')

        place.booked_on = None
        place.user = None
        place.save()

        return redirect('profile')


class ProfilePage(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    @staticmethod
    def get(request):
        user_places = RestaurantPlace.objects.filter(user=request.user).order_by('booked_on')

        context = {
            'user_places': user_places,
            'UserEditForm': UserEditForm(instance=request.user)
        }
        return render(request, 'restaurants/profile.html', context)

    @staticmethod
    def post(request):
        form = UserEditForm(request.POST, instance=request.user)
        if not form.is_valid():
            return render(request, 'restaurants/profile.html', {'UserEditForm': form})

        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        if password:
            user.set_password(password)
        user.save()

        updated_user = authenticate(username=user.username, password=password)
        if updated_user is not None:
            login(request, updated_user)

        return redirect('profile')
