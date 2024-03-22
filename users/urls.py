from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login-page'),
    path('registration/', views.registration_view, name='registration-page')
]