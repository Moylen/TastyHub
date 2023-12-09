from django.urls import path

from .views.SetAllFree import SetAllFree
from .views.SetBookedOccupied import SetBookedOccupied
from .views.SetOccupiedFree import SetOccupiedFree
from .views.Index import Index
from .views.AccountPage import AccountPage
from .views.Reserve import Reserve
from .views.SetBookedFree import SetBookedFree
from .views.RestaurantBookingPage import RestaurantBookingPage
from .views.RestaurantManagePage import RestaurantManagePage
from .views.RestaurantMenuPage import RestaurantMenuPage
from .views.RestaurantPage import RestaurantPage

urlpatterns = [
    path('', Index.as_view(), name='index'),

    path('restaurant/booking/<int:pk>', RestaurantBookingPage.as_view(), name='booking'),
    path('restaurant/<int:pk>', RestaurantPage.as_view(), name='restaurant'),
    path('restaurant/menu/<int:pk>', RestaurantMenuPage.as_view(), name='menu'),
    path('restaurant/manage', RestaurantManagePage.as_view(), name='manage'),

    path('account', AccountPage.as_view(), name='account'),

    # Для админ-панели
    path('occupy/<int:pk>', SetBookedOccupied.as_view(), name='setBookedOccupied'),
    path('free/<int:pk>', SetOccupiedFree.as_view(), name='setOccupiedFree'),
    path('reserve/delete/<int:pk>', SetBookedFree.as_view(), name='setBookedFree'),
    path('free/all/<int:pk>', SetAllFree.as_view(), name='setAllFree'),

    # Для пользователя через форму
    path('reserve/<int:pk>', Reserve.as_view(), name='reserve')
]
