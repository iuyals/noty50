from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "user/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "user/user.html", context)

def login_view(request):
    name = request.POST["username"]
    passwd = request.POST["password"]
    print(name)
    print(passwd)
    user = authenticate(request, username=name, password=passwd)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("userhome"))
    else:
        return render(request, "user/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "user/login.html", {"message": "you have logged out.\n  log in again below"})

def register_view(request):
    if request.method=="GET":
        return render(request,"user/register.html",{})
        
    name = request.POST["username"]
    password = request.POST["password"]
    passwordagain=request.POST["passwordagain"]
    if len(name) <3 or len(password) <6:
        return render(request,'notice.html',{'msg':'user name or password too short'})
    if password!=passwordagain:
        return render(request,'notice.html',{'msg':'two password not match'})
    if(User.objects.all().filter(username=name)):
        return render(request,'notice.html',{'msg':'user already exist,choose anothe name'})
    newuser=User()
    newuser.username=name
    newuser.set_password(raw_password=password)
    newuser.save()
    
    return render(request,"user/register.html",{})