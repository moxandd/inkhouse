from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def home_view(request):

    categories = Category.objects.all()
    products = Product.objects.all()
    page_name = 'Home'

    if request.GET.get('category') == "all" or request.GET.get('category') is None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category=request.GET.get('category'))


    return render(request, 'core/homepage.html', context={'page_name': page_name, 'products': products, 'categories': categories})