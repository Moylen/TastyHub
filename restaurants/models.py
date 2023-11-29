from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class KitchenType(models.Model):
    
    # Ценность типа ресторана(по макету)
    worthes = [
        ('Низкая', 'Низкая'),
        ('Средняя', 'Средняя'),
        ('Высокая', 'Высокая')
    ]
    
    name = models.CharField(max_length=32, blank=False, null=False)
    worth = models.CharField(max_length=16, choices=worthes, default='Низкая')
    
    def __str__(self):
        return f'{self.name}'


class Restaurant(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    avg_check = models.FloatField(default=0, blank=False, null=False)
    address = models.CharField(max_length=128, blank=False, null=False)
    contacts = models.CharField(max_length=128, blank=False, null=False)
    description = models.CharField(max_length=512, blank=False, null=False)
    logo = models.ImageField(upload_to='restaurant_logos', blank=False, null=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    
    admin_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    kitchen_type = models.ForeignKey(KitchenType, on_delete=models.SET_NULL, null=True)
    
    
class RestaurantPlace(models.Model):
    
    # Тип кресла
    types = [
        ('Мягкий', 'Мягкий'), ('Твердый', 'Твердый')
    ]
    
    number = models.IntegerField(default=0, blank=False, null=False)
    place_amount = models.IntegerField(default=1, blank=False, null=False) 
    type = models.CharField(max_length=16, choices=types, blank=False, null=False)
    
    is_occupied = models.BooleanField(default=False)
    occupied_in = models.DateTimeField(default=None)
    is_booked = models.BooleanField(default=False)
    booked_on = models.DateTimeField(default=None)
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    
class RestaurantReview(models.Model):
    
    # Возможные оценки ресторана
    marks = [
        ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)
    ]
    
    mark = models.IntegerField(choices=marks, blank=False, null=False)
    comment = models.TextField(max_length=1024, blank=False, null=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    

class RestaurantImage(models.Model):
    image = models.ImageField(upload_to='restaurant_images', blank=False, null=False)
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    

class RestaurantMeal(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    date_create = models.DateTimeField(auto_now_add=True)
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    

class MealImage(models.Model):
    image = models.ImageField(upload_to='meal_images/%Y/%m/%d/', blank=False, null=False)
    
    restaurant_meal = models.ForeignKey(RestaurantMeal, on_delete=models.CASCADE)
    