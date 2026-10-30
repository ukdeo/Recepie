# from django.db import models

# # Create your models here.
# class Students(models.Model):
#     name = models.CharField(max_length=16)
#     age = models.IntegerField()
#     Email = models.EmailField(max_length=30)
#     address = models.TextField(max_length=100)
#     image = models.ImageField(upload_to="images", null=True, blank=True)

# class Product(models.Model):
#     id =models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=16)
#     price = models.IntegerField()
#     description = models.TextField(max_length=100)
#     image = models.ImageField(upload_to="images", null=True, blank=True)

#     def __str__(self):
#         return self.name
