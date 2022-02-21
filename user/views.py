from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

from user.form import UserForm

# Create your views here.
def adminlogin(request):
    if request.method =='POST':
        un = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=un,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/user/admindashboard')
        else:
            return redirect('/user/adminlogin')
        
    return render(request,'user/login.html')
def adminregister(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('/user/adminlogin')
    return render(request,'user/register.html')
def admindashboard(request):
    users = User.objects.all()
    return render(request,'user/dashboard.html',{'users':users})
def adminedit(request,id):
        user = User.objects.get(id=id)
        return render(request,'user/edit.html',{'user':user})

def adminupdate(request,id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST,instance=user)
    if form.is_valid:
        form.save()
        return redirect('/user/admindashboard')
    return render(request,'user/edit.html',{'user':user})
def admindelete(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/user/admindashboard')


    