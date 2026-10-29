from django.shortcuts import redirect, render
from .models import Recepie
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('recepie')

        messages.error(request, 'Invalid username or password')
        return redirect('login')

    return render(request, 'login.html')

#for login and register we will use the built in user model of django which is imported above
def register(request):

    if request.method == 'POST':
        data = request.POST

        username =  data.get('username')
        email =data.get('email')
        password =data.get('password')

# to check if the username already exists in the database we will use the filter method of the user model which is imported above
        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username already exists')
            return render(request, 'register.html')

        user = User.objects.create_user(
            username=username, 
            email=email,
           )
        user.set_password(password)
        user.save()
        messages.success(request, 'Account created successfully. Please sign in.')
        return redirect('login')

    
    return render(request, 'register.html')
