from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
# Create your views here.

def recepie(request):
    if request.method == 'POST':
        data = request.POST

        name =  data.get('name')
        description =data.get('description')
        image =request. FILES.get("image")

        # print(image)
        # print(name)
        # print(description)

        Recepie.objects.create(
            name = name,
            description = description,
            image=image
        )

      

    queeryset = Recepie.objects.all()
    
    return render(request, 'recepie.html', context = {'recepie': queeryset })


def login(request):
    return render(request, 'login.html')
def register(request):

    if request.method == 'POST':
        data = request.POST

        username =  data.get('username')
        email =data.get('email')
        password =data.get('password')

        print(username)
        print(email)
        print(password)

        user = User.objects.create_user(
            username=username, 
            email=email,
           )
        user.set_password(password)
        user.save()

        return redirect('login')
    return render(request, 'register.html')

