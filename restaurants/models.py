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
    description = models.TextField(max_length=512, blank=False, null=False)
    working_mode = models.TextField(max_length=64, blank=False, null=False)
    logo = models.ImageField(upload_to='restaurant_logos', blank=False, null=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)

    admin_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    kitchen_type = models.ForeignKey(KitchenType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'


class RestaurantPlace(models.Model):
    # Тип кресла
    types = [
        ('Мягкий', 'Мягкий'), ('Твердый', 'Твердый')
    ]

    # Тип стола
    table_sizes = [
        ('table-small', 'Маленький'), ('table-medium', 'Средний'), ('table-large', 'Большой'),
        ('table-medium-vertical', 'Средний (вертикальный)'), ('table-large-vertical', 'Большой (вертикальный)')
    ]

    # Номер стола в конкретном ресторане
    local_number = models.IntegerField(default=0, blank=False, null=False)

    # Размер стола
    table_size = models.CharField(max_length=32, choices=table_sizes, blank=False, null=False)

    # Расположение стола в ресторане
    location_x = models.FloatField(blank=False, null=False, default=0)
    location_y = models.FloatField(blank=False, null=False, default=0)

    # Тип сиденья
    type = models.CharField(max_length=16, choices=types, blank=False, null=False)

    # Количество мест
    place_amount = models.IntegerField(blank=False, null=False, default=0)

    # Если установлено время, то оно занято
    occupied_in = models.TimeField(default=None, blank=True, null=True)

    # Если установлено время, то оно забронировано
    booked_on = models.TimeField(default=None, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.restaurant.name} | {self.local_number} стол'


class RestaurantReview(models.Model):
    # Возможные оценки ресторана
    marks = [
        (1, '\u2605'),
        (2, '\u2605\u2605'),
        (3, '\u2605\u2605\u2605'),
        (4, '\u2605\u2605\u2605\u2605'),
        (5, '\u2605\u2605\u2605\u2605\u2605')
    ]

    mark = models.IntegerField(choices=marks, blank=False, null=False)
    comment = models.TextField(max_length=1024, blank=True, null=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}'


class RestaurantImage(models.Model):
    image = models.ImageField(upload_to='restaurant_images', blank=False, null=False)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class RestaurantMeal(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    date_create = models.DateTimeField(auto_now_add=True)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.restaurant.name}'


class MealImage(models.Model):
    image = models.ImageField(upload_to='meal_images/%Y/%m/%d/', blank=False, null=False)

    restaurant_meal = models.ForeignKey(RestaurantMeal, on_delete=models.CASCADE)
