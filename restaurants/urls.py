from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('restaurant/<int:pk>', views.RestaurantPage.as_view(), name='restaurant'),
    path('reserve/<int:pk>', views.Reserve.as_view(), name='reserve'),
    path('profile/', views.ProfilePage.as_view(), name='profile'),
    path('reserve/delete/<int:pk>', views.ReserveDelete.as_view(), name='reserve_delete')
]
