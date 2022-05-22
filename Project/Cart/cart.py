from decimal import Decimal
from django.conf import settings
from Shop.models import product

class Cart(object):
	"""docstring for Cart"""
	def __init__(self, request):
		"""initalize the cart"""
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

###########################################################

	def add(self,Product):
		product_id = str(Product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'price':str(Product.price)}
		self.save()

###########################################################

	def save(self):
		self.session[settings.CART_SESSION_ID] = self.cart
		self.session.modified = True

###########################################################

	def remove(self,product):
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()
			
###########################################################

	def __iter__(self):
		product_ids = self.cart.keys()
		products = product.objects.filter(id__in=product_ids)
		for Product in products:
			self.cart[str(Product.id)]['Product'] = Product
		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			yield item

###########################################################

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		del self.session['coupon_id']
		self.session.modified = True