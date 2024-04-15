from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_view, name='home'),
    path('product/<int:pk>/', views.product_view, name='product')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)