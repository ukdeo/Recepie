from django.db import models

# Create your models here.
class Recepie(models.Model):
    name = models.CharField(max_length=16)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to="images", null=True, blank=True)

   