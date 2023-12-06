from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.UserRegistrationPage.as_view(), name='registration'),
    path('login/', views.UserLoginPage.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout')
]
