from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View

from restaurants.forms import ReviewForm
from restaurants.models import Restaurant, RestaurantReview


class SetReview(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    @staticmethod
    def post(request, pk):
        form = ReviewForm(request.POST)
        if not form.is_valid():
            messages.error(request, 'Ошибка отправки отзыва')
            return redirect(reverse('restaurant', kwargs={'pk': pk}))

        # Если пользователь уже оставлял отзыв на этот ресторан
        if RestaurantReview.objects.filter(author=request.user, restaurant=pk):
            messages.error(request, 'Вы уже оставляли отзыв')
            return redirect(reverse('restaurant', kwargs={'pk': pk}))

        review = form.save(commit=False)
        review.author = request.user
        review.restaurant = Restaurant.objects.get(pk=pk)
        review.save()

        return redirect(reverse('restaurant', kwargs={'pk': pk}))
