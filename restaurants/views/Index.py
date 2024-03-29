from django.shortcuts import render
from django.views import View

from restaurants.forms import FilterForm
from restaurants.models import Restaurant, RestaurantImage


class Index(View):
    @staticmethod
    def get(request):
        restaurants = Restaurant.objects.all()

        context = {'FilterForm': FilterForm(), 'restaurants': restaurants}
        return render(request, 'restaurants/index_page.html', context)

    @staticmethod
    def post(request):
        form = FilterForm(request.POST or None)
        if not form.is_valid():
            return render(request, 'restaurants/index_page.html', {'FilterForm': form})

        if form.cleaned_data['name'] is None:
            restaurants = Restaurant.objects.all()
        else:
            kitchen_type = form.cleaned_data['name']
            restaurants = Restaurant.objects.filter(kitchen_type=kitchen_type)

        context = {'FilterForm': form, 'restaurants': restaurants}
        return render(request, 'restaurants/index_page.html', context)
