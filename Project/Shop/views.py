from django.shortcuts import render
from .models import category,product
# Create your views here.

def index(request):
    allcategory = category.objects.all()
    allproduct = product.objects.all()
    return render(request, 'shop/index.html' , {'allproduct':allproduct , 'allcategory':allcategory})

def shop(request,categoryid):
    allcategory = category.objects.all()
    mycategory = category.objects.get(id = categoryid)
    allproduct = product.objects.filter(category_id = categoryid)
    return render(request, 'shop/shop.html', {'allproduct':allproduct , 'allcategory':allcategory , 'mycategory' : mycategory})

def detail(request,productid):
    allcategory = category.objects.all()
    myproduct = product.objects.get(id = productid)
    return render(request, 'shop/detail.html' , {'allcategory':allcategory , 'myproduct' : myproduct})

def Product(request):
    allcategory = category.objects.all()
    allproduct = product.objects.all().order_by("-id")
    return render(request, 'shop/product.html' , {'allproduct':allproduct , 'allcategory':allcategory})

def cart(request):
    allcategory = category.objects.all()
    allproduct = product.objects.all()
    return render(request, 'shop/store.html' , {'allproduct':allproduct , 'allcategory':allcategory})

def contact(request):
    return render(request, 'shop/contact.html')