from django.shortcuts import render,redirect
from . models import Catalyst


# Create your views here.
def create_Catalyst(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['age']
        course=request.POST['course']
        Catalyst.objects.create(name=name,email=email,course=course)
        return redirect('view_list')
    return render(request,'app/add.html')
    
def view_list(request):
        catalyst = Catalyst.objects.all()
        return render(request,'app/list.html', {'catalyst':catalyst})

