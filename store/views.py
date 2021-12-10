from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from .utils import *

import json
import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *



# Create your views here.
def p404(request):
    context = {}
    return render(request, 'store/404-page.html', context)

def index(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    products = checkIfItemInCart(request , items)


    context = {'products':products, 'cartItems':cartItems }
    return render(request, 'store/index.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
    

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        
        if total == order.get_cart_total:
            order.complete = True
            order.delevery_fee= 5
        order.save()
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['state'],
	)
        print(data['shipping']['address'])


    else:
        print('User is not logged in')

    return JsonResponse('Payment submitted..', safe=False)



    order_success

def order_success(request):
    context = {}
    return render(request, 'store/order-success.html', context)

def wishlist(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        wishlist =customer.wish_list.all()

    
        for product in wishlist:
            for item in items:
                if product.id == item.product.id:
                    product.quantity =  item.quantity
    else:
        customer = ''
        wishlist = ''
        



    
    context = {"wishlist":wishlist,'customer':customer}
    return render(request, 'store/wishlist.html', context)

@api_view(['GET'])
def product_details(request):
    product = Product.objects.get(id = 1)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


