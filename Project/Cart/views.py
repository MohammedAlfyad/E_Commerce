from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from Shop.models import product , category
from .cart import Cart
# Create your views here.

@require_POST
def cart_add(request,Product_id):
	cart = Cart(request)
	Product = get_object_or_404(product,id=Product_id)
	cart.add(
		Product=Product
		)
	return redirect('cart:cart_detail')

def cart_remove(request,Product_id):
	cart = Cart(request)
	Product = get_object_or_404(product,id=Product_id)
	cart.remove(Product)
	return redirect('cart:cart_detail')

def cart_detail(request):
	cart = Cart(request)
	categories = category.objects.all()
	return render(request,'shop/cart.html',{'cart':cart,'categories':categories})