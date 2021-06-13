from django.urls import path
from mylist import views

urlpatterns = [
    # Home page Url
    path('', views.home, name='home'),
    path('addProduct', views.addProduct, name='addProduct'),
    path('addToCart', views.addToCart, name='addToCart'),
    path('removeFromCart', views.removeFromCart, name='removeFromCart'),
    path('mycart', views.mycart, name='myCart'),
]
