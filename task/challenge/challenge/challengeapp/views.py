from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import place
from .models import team
from django.http import HttpResponse
# Create your views here.
def demo(request):
    obj=place.objects.all()
    teamobj=team.objects.all()
    return render(request,"index.html",{'objs':obj,'teamobject':teamobj})

#def home(request):
 # return HttpResponse("this is home")

def about(request):
    return render(request,"about.html")

def contact(request):
    return HttpResponse("this is contact")


def details(request,id):
    movies=movie.objects.get(id=id)

    return render(request,"details.html",{'movie':movies})

#def home(request):
#    return  render(request,"home.html")

def thanks(request):
    return  HttpResponse("this is for thanks")


def addition(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res = x + y
    results=x*y
    resul=x//y
    rest=x-y
    return render(request,"result.html",{'result':res,'mul':results,'div':resul,'sub':rest})


# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if cpassword==password:
            if User.objects.filter(username=username).exists():
               messages.info(request,"user already exist")
               return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect(register)
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();
                return redirect(login)
        else:
            messages.info(request,"Password mismatches")
            return redirect(register)
        return redirect('/')
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect(login)

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


