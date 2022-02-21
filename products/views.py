from django.shortcuts import render,redirect

from products.forms import ProductsForm
from products.models import Products

# Create your views here.
def view(request):
    products = Products.objects.all()
    return render(request,'product/view.html',{'products':products})
def add(request):
    if request.method == 'POST':
        print(request.FILES)
        form = ProductsForm(request.POST,request.FILES)
        print(form)
        form.save()
        return redirect('/product/view')
    else:
        form = ProductsForm()

    return render(request,'product/add.html',{'form':form})
def edit(request,id):
    product = Products.objects.get(id=id)
    return render(request,'product/edit.html',{'product':product})
def update(request,id):
    product = Products.objects.get(id=id)
    form = ProductsForm(request.POST,instance=product)
    if form.is_valid:
        form.save()
        return redirect('/product/view')
    return render(request,'product/edit.html',{'product':product})
def delete(request,id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('/product/view')