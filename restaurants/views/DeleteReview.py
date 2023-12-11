from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

from restaurants.models import RestaurantReview


class DeleteReview(View):
    @staticmethod
    def get(request, pk):
        review = RestaurantReview.objects.get(pk=pk)
        restaurant_id = review.restaurant_id

        if review.author != request.user:
            return redirect(reverse('restaurant', kwargs={'pk': restaurant_id}))

        review.delete()
        return redirect(reverse('restaurant', kwargs={'pk': restaurant_id}))
