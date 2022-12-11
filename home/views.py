from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable":"This is sent "
    }
   
    return render(request,'index.html',context)
    # return HttpResponse("This is homepage")

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
  