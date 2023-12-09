from django import forms
from .models import KitchenType, RestaurantPlace


class FilterForm(forms.Form):
    name = forms.ModelChoiceField(
        queryset=KitchenType.objects.filter(restaurant__isnull=False).distinct(),
        empty_label='Все кухни',
        widget=forms.Select(attrs={'class': 'form-control'}),
        label=False,
        required=False
    )


class BookingForm(forms.ModelForm):
    booked_on = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))

    class Meta:
        model = RestaurantPlace
        fields = ['booked_on', ]
