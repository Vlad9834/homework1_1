from django.db import models

# Create your models here.

class AutoModel(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
