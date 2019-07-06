from django.shortcuts import render,HttpResponse

# Create your views here.
from django.contrib.auth import authenticate,logout,login
from django.shortcuts import render,HttpResponse,redirect
from .forms import UserRegisterForm

def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserRegisterForm(request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(user_form.errors)
    else:
        user_form=UserRegisterForm()
    return render(request,'auth/register.html',{'form':user_form,'registered':registered})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_activate:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("your")    
        else:
            print("someone tried to login and failed")   
            print("They used username:{} and password: {}".format(username,password))
            return HttpResponse("Invalid login")
    else:
        return render(request,'auth/login.html',{})

def user_logout(request):
    logout(request)
    return redirect('/')         
    


def home_view(request):
    return render(request,'testpage.html')
