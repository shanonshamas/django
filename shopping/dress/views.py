from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        User.objects.create_user(
            username=username,
            password=password
        )
        
        return redirect('login')
    return render(request, 'register.html')

from django.contrib.auth import authenticate,login

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(
            username=username,
            password=password
        )
        
        if user is not None:
            login(request,user)
            return redirect('profile')
        
        return render(request,'login.html',{
            'error':'Invalid username or password'
            })
    
    return render(request,'login.html')



from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('login')


from django.contrib.auth.decorators import login_required

@login_required

def profile(request): 
    if request.user.is_authenticated:
        print("User is logged in")
    else:
        print("User is not logged in")
    
    return render(request,'profile.html')