from django.shortcuts import redirect, render
from booking.forms import BookingForm

from products.models import Products
from django.contrib import auth

# Create your views here.


def bookingnew(request,id):
    product = Products.objects.get(id=id)
    return render(request,'booking.html',{'product':product})

def bookingfinal(request):
    if request.method == 'POST':
        print(request.FILES)
        form = BookingForm(request.POST,request.FILES)
        print(form)
        form.save()
        return redirect('/')
    else:
        form = BookingForm()
    return render(request,'booking.html',{'form':form})