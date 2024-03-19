from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"