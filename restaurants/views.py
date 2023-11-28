from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class Index(View):
    @staticmethod
    def get(request):
        return render(request, 'restaurants/index.html')
