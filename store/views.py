
from django.shortcuts import render,redirect
from customer.models import Customer
from products.models import Products
from store.forms import ContactForm

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]

        try:
            customer=Customer.objects.get(username=username,password=password)
            request.session['customer_id']=customer.customer_id
            return redirect('/')
        except:
            print("invalid")
    return render(request,'login.html')


    return render(request,'register.html')

def home(request):

    keyring = Products.objects.filter(type='keyring')
    bag = Products.objects.filter(type='bag')
    statue = Products.objects.filter(type='statue')

    return render(request,'index.html',{'keyring':keyring,'statue':statue,'bag':bag})
    
def admin(request):
    return render(request,'AdminDashboard.html')

def signout(request):
    request.session.clear()
    return redirect("/")

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        form.save()
    else:
        form=ContactForm()
    return redirect("/")
