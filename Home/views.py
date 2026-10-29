from django.shortcuts import render
from django.http import HttpResponse

from Home.models import *
from recepie.models import *


# Create your views here.

# def home(request):

#     # students = [
#     #     {
#     #         'name': "UDAY KUMAR DEV",
#     #         'age': 45.
#     #     },

#     #     {
#     #         'name': "Ram KUMAR DEV",
#     #         'age': 45,
#     #     }
#     # ]

#     # for student in students:
#     #     print(student)

#     return render(request, "index.html", context={"peoples": Students,"page": "Home"})

def home(request):
    return render(request, "index.html", context={"page": "Home"})

def about(request):
   context = {"page": "About "}
   return render(request, "about.html",context=context)

def contact(request):
    
    return render(request, "contact.html",context = {"page": "contact"})