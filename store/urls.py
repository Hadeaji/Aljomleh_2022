
from django.urls import path

from . import views

urlpatterns = [
	path('404', views.p404, name="store"),
	path('', views.index, name="index"),
	path('checkout', views.checkout, name="checkout"),
    path('order-success', views.order_success, name="order-success"),
    path('wishlist', views.wishlist, name="wishlist"),


    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('product_details/', views.product_details, name="product_details"),


    



]