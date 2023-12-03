from django.shortcuts import render
from django.views.generic import View
from .forms import FilterForm
from .models import Restaurant

# Create your views here.


class Index(View):
    @staticmethod
    def get(request):
        restaurants = Restaurant.objects.all()
        context = {
            'FilterForm': FilterForm(),
            'restaurants': restaurants
        }
        return render(request, 'restaurants/index.html', context)
    
    @staticmethod
    def post(request):
        form = FilterForm(request.POST)
        if form.is_valid():
            kitchen_type = form.cleaned_data['name']
            restaurants = Restaurant.objects.filter(kitchen_type=kitchen_type)
            context = {
                'FilterForm': form,
                'restaurants': restaurants
            }
            return render(request, 'restaurants/index.html', context)
        return render(request, 'restaurants/index.html', {'FilterForm': form})
    

class RestaurantPage(View):
    @staticmethod
    def get(request, pk):
        restaurant = Restaurant.objects.get(pk=pk)
        return render(request, 'restaurants/booking_page.html', {'restaurant': restaurant})
