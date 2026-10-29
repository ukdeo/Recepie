from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recepie(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=16)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to="images", null=True, blank=True)

   