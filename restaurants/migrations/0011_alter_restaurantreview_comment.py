# Generated by Django 4.2.7 on 2023-12-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_alter_restaurantreview_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantreview',
            name='comment',
            field=models.TextField(blank=True, max_length=1024),
        ),
    ]