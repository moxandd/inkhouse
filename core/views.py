from django.shortcuts import render

# Create your views here.

def home_view(request):
    page_name = 'Home'
    return render(request, 'core/homepage.html', context={'page_name': page_name})