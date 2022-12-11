from django.shortcuts import render,redirect, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request,'index.html')
    # return HttpResponse("This is homepage")

def loginUser(request):
    # password for test user is 075bct034, pulchowkcampus
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def about(request):
    return render(request,'about.html')
    

def departments(request):
    return render(request,'departments.html')
    

def contact(request):
    if request.method=='POST':

        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your form has been submitted!x')

    return render(request,'contact.html')
  