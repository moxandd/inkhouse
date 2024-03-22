from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login-page'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.registration_view, name='registration-page'),
    path('password_recovery/', views.password_recovery_view, name='password-recovery')
]