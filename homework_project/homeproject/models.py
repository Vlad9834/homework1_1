from django.db import models

# Create your models here.

class AutoModel(models.Model):
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    factory = models.ForeignKey('Brand',on_delete=models.CASCADE,related_name="cars",blank=True,null=True)
class Brand(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


