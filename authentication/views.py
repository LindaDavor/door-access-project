from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
# from django.contrib.auth.models import *
from django.db import IntegrityError
from .models import *


# Create your views here.

# login user view which authenticate the user
def login_user_view(request):

    if request.method == "POST":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username = username , password = password)
        print(user)

        
        if user.is_user == True:
            login(request, user)
            return redirect("main:user_dashboard")

        elif user.is_service_provider == True:
            login(request, user)
            return redirect("main:service_provider_dashboard")

        elif username =="admin":
            return redirect("dashboard:admin_dashboard")

        else:
            return HttpResponse("try again")

    return render(request,'login.html')


# register user view which saves the user details in the data base
def register_user_view(request):

    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        get_level = request.POST['user']
       
       # this deals with the radio button selection
        if get_level == 'User':

            user = MyData.objects.create(
                username = username,
                email = email,
                is_user = True
            )
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("yes is user")

        elif get_level == 'Service_Provider':
            user = MyData.objects.create(
                username = username,
                email = email,
                is_service_provider = True
            )
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("yes is service")
        user.set_password(password)
        user.save()

        return redirect("auth:user_authentication")

    else:
        pass
    return render(request,'register/signup_user.html')

