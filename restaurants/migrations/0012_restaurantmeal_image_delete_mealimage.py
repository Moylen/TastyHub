# Generated by Django 4.2.7 on 2023-12-12 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0011_alter_restaurantreview_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantmeal',
            name='image',
            field=models.ImageField(null=True, upload_to='meal_images/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='MealImage',
        ),
    ]