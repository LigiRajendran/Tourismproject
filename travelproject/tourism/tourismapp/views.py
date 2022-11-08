from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from tourismapp.models import Team, Place


def index(request):
    obj=Team.objects.all()
    obj1 = Place.objects.all()
    return render(request,"index.html",{'result':obj, 'place':obj1})
# Create your views here.
def registration(request):
     if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repass']

        if password==repassword:

          if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exist")
            print("Username already exist")
            return redirect('/registration')
          elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already exist")
            print("Email already exist")
            return redirect('/registration')
          else :
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                            password=password)
            messages.info(request, "Registration successfully completed")
            print("User created")
            return redirect('/registration')
        else:
            print("password not matching")
            messages.info(request,"password not matching")
            return redirect('/registration')
     return render(request,"registration.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credential")

            return redirect('/login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

