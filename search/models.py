from django.db import models

# Create your models here.

class Car(models.Model):
    model_year
    registered_day
    brand
    type
    model
    car
    fuel
    gear
    kms
   region
   status
   photo(models.FileField(null=True))