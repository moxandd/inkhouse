from django.contrib import admin
from .models import Product, Author, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Author)
admin.site.register(Category)