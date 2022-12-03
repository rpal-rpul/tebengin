from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from dashboard_customer.models import Driver, Customer, Review, DashboardCustomer
from django.contrib.auth.models import User
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from dashboard_driver.models import OrderStatus
import json

# Create your views here.
@csrf_exempt
def add_review(request):
    print(request.POST)
    print(request.user.id)
    if request.method == 'POST':
        id_customer = request.POST["id_customer"]
        id_driver = request.POST["id_driver"]
        message = request.POST["isi"]

        customer = User.objects.get(pk=id_customer)
        driver = User.objects.get(pk=id_driver)
        customer_login = User.objects.get(pk=request.user.id)

        print("ini driver", driver)
        print("ini cust", customer_login)
        # Create object
        Review.objects.create(message=message, driver=driver, customer=customer_login)
        return HttpResponse({})
        
@csrf_exempt
def get_review(request):
    if request.method == 'GET':
        data = list(Review.objects.values())
        return JsonResponse(data, safe=False)

@csrf_exempt
def get_review_driver(request):
    if request.method == 'GET':
        driver_login = User.objects.get(pk=request.user.id)
        
        data = list(driver_login.review_set.all())
        return JsonResponse(data, safe=False)

@csrf_exempt
def getCustomerOrder(request):
    user = request.user
    if user.is_anonymous:
        return JsonResponse({"error": "Belum login"}, status=200)
    customer = Customer.objects.get(user=user)
    dashboard_customer = DashboardCustomer.objects.get(customer=customer)

    value = {
        "accepted_order": list(dashboard_customer.order.filter(status=OrderStatus.ACCEPTED)),
        "rejected_order": list(dashboard_customer.order.filter(status=OrderStatus.REJECTED)),
        "pending_order": list(dashboard_customer.order.filter(status=OrderStatus.PENDING)),
        "history_order": list(dashboard_customer.order.filter(status=OrderStatus.FINISHED)),
    }

    return render(request, "dashboard_customer/index.html", value)