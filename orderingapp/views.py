from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AddProduct, PlaceOrder
from .forms import AddProductForm, updateStatusForm, OrderForm, OrdersFormSet


# Create your views here.

@login_required
def userDashboard(request):
    return render(request, 'user-dash.html')

@login_required
def placeOrder(request, id):
    username = request.user
    productDetail = AddProduct.objects.get(pk=id)
    form = OrderForm()
    formset = OrdersFormSet()
    context = {'productDetail': productDetail, 'username': username,'form':form,'formset':formset}
    if request.method == 'POST':
        if request.POST.get('product_quantity'):
            orderModel = PlaceOrder()
            orderModel.product_name = request.POST['product_name']
            orderModel.product_description = request.POST['product_description']
            orderModel.product_price = request.POST['product_price']
            orderModel.order_by = request.POST['order_by']
            orderModel.product_quantity = request.POST['product_quantity']
            orderModel.product_status = request.POST['product_status']

            orderModel.save()
            return redirect('user-dashboard')
    return render(request, 'order.html', context)

def showOrderHistory(request):
    username = request.user
    orderDetail = PlaceOrder.objects.filter(order_by=username)
    print(orderDetail)
    context = {'orderDetail': orderDetail}

    return render(request, 'previousorders.html', context)

