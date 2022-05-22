from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name = 'index'),
    path('category/<int:categoryid>/' , views.shop , name = 'Shop'),
    path('product/<int:productid>/' , views.detail , name = 'detail'),
    path('product.html' , views.Product , name = 'product'),
    path('store.html' , views.cart , name = 'cart'),
    path('contact.html' , views.contact , name = 'contact'),
]
