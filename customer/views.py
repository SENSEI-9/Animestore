from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def register(request):
    if request.method == "POST":
        print(request.POST)
        form = CustomerForm(request.POST)
        form.save()
        return redirect("/login")
    else:
        form = CustomerForm()
    return render(request, "register.html", {'form': form})
