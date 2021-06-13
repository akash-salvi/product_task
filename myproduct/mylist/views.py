from django.shortcuts import redirect, render
from django.http import HttpResponse  , HttpResponseRedirect
from .models import Products,Cart
from datetime import date


# Create your views here.

def home(request):
    products=Products.objects.all()
    return render(request, 'home.html',{'products':products})

def addProduct(request):
    if request.method == 'POST':
        prod_name = request.POST["name"]
        prod_price = request.POST['price']
        prod_desc = request.POST['desc']
        prod_number = request.POST['number']
        
        prod_image= request.FILES['image']

        product=Products();
        product.product_name=prod_name;
        product.price=prod_price
        product.desc=prod_desc
        product.product_number=prod_number;
        product.image=prod_image;
        product.save();

        products=Products.objects.all()
        return render(request, 'home.html',{'products':products})
    else:
        messages.info(request, "404 Not Found!")
        return redirect('handlerror')
        
def addToCart(request):
    if request.method == 'POST':
        item_number = request.POST['number']

        item=Products.objects.get(product_number=item_number)
    
        product=Cart();
        product.product_name=item.product_name;
        product.price=item.price
        product.desc=item.desc
        product.product_number=item.product_number;
        product.image=item.image;
        product.date=date.today()
        product.save();

        products=Products.objects.all()
        
        return render(request, 'home.html',{'products':products,'flag':True})
    else:
        messages.info(request, "404 Not Found!")
        return redirect('handlerror')

def mycart(request):
    cart=Cart.objects.all()
    return render(request, 'mycart.html',{'cart':cart})

def removeFromCart(request):
    if request.method == 'POST':
        item_number = request.POST['number']

        item=Cart.objects.get(product_number=item_number)
    
        item.delete()

        cart=Cart.objects.all()
        return render(request, 'mycart.html',{'cart':cart})
    else:
        messages.info(request, "404 Not Found!")
        return redirect('handlerror')


        
