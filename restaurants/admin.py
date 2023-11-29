from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Restaurant)
admin.site.register(models.RestaurantImage)
admin.site.register(models.RestaurantPlace)
admin.site.register(models.RestaurantReview)
admin.site.register(models.RestaurantMeal)
admin.site.register(models.MealImage)
admin.site.register(models.KitchenType)

