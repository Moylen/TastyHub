from django.shortcuts import render
from django.views import View

from restaurants.forms import ReviewForm
from restaurants.models import Restaurant, RestaurantMeal, RestaurantReview, RestaurantImage


class RestaurantPage(View):
    @staticmethod
    def get(request, pk):
        restaurant = Restaurant.objects.get(pk=pk)
        meals = RestaurantMeal.objects.filter(restaurant=restaurant)
        reviews = RestaurantReview.objects.filter(restaurant_id=pk)
        restaurant_images = RestaurantImage.objects.filter(restaurant=restaurant)

        context = {
            'restaurant': restaurant,
            'restaurant_images': restaurant_images,
            'meals': meals,
            'ReviewForm': ReviewForm(),
            'reviews': reviews
        }
        return render(request, 'restaurants/restaurant_page.html', context)

