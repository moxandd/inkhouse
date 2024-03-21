from django.shortcuts import render
from .models import Product

# Create your views here.

def home_view(request):
    products = Product.objects.all()
    page_name = 'Home'
    return render(request, 'core/homepage.html', context={'page_name': page_name, 'products': products})