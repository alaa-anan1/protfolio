from django.db import models


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=100)
    disceiption = models.TextField()
    image = models.FilePathField(path="/img")


class Trip(models.Model):
    trip_number = models.URLField(
        ("Trip Number"), 
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )






# NOTESS FOR LATER ::::  make a new model for the image and delete the object from About and makemigtations --> migrate 