from django.shortcuts import render
from .models import *

# Create your views here.

def recepie(request):
    if request.method == 'POST':
        data = request.POST

        name =  data.get('name')
        description =data.get('description')
        image =request. FILES.get("image")

        print(image)
        print(name)
        print(description)

        Recepie.objects.create(
            name = name,
            description = description,
            image=image
        )

        # return redirect('/recepie/')

    queeryset = Recepie.objects.all()
    
    return render(request, 'recepie.html', context = {'recepie': queeryset })