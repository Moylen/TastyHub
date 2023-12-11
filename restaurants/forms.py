from django import forms
from .models import KitchenType, RestaurantPlace, RestaurantReview


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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = RestaurantReview
        fields = ['mark', 'comment']
        widgets = {
            'mark': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'text', 'style': 'min-height: 150px;'})
        }
