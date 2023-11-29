from django import forms
from .models import KitchenType


class FilterForm(forms.Form):
    name = forms.ModelChoiceField(
        queryset=KitchenType.objects.filter(restaurant__isnull=False).distinct(), 
        empty_label='Все кухни',
        widget=forms.Select(attrs={'class': 'form-control'}),
        label=False,
        # required=False # Если нужно будет сделать фильтрацию по всем объектам, при empty_label
    )

