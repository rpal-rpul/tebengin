from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from dashboard_customer.models import Driver, Customer, Review, DashboardCustomer
from django.contrib.auth.models import User
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from dashboard_driver.models import OrderStatus

from authentication.models import Pengguna
from django.core import serializers
import json
from main.views import check_user_role
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
@login_required(login_url='/authentication/login/')
def add_review(request):
    user_id = request.user.id
    is_driver = check_user_role(request.user)
    context = {
            'is_driver': is_driver,
        }
    customer = User.objects.get(pk=user_id)

    if request.method == 'POST':
        message = request.POST["review_message"]
        driver = User.objects.get(pk=request.POST["driver_id"])
        Review.objects.create(message=message, driver= driver,customer=customer)
        return JsonResponse({"success":"Success to add review"}, status=200)

    return JsonResponse({"failed": "Not using right method"}, status=405)

        
@csrf_exempt
def get_review(request):
    if request.method == 'GET':
        data = list(Review.objects.values())
        return JsonResponse(data, safe=False)

@csrf_exempt
def get_review_driver(request):
    if request.method == 'GET':
        driver_login = User.objects.get(pk=request.user.id)

        all_review = Review.objects.all()
        print(request.user.id)
        print(all_review)
        review_driver = []
        for i in all_review:
            if i.driver == driver_login:
                review_driver.append(i)
        print(review_driver)

        serialized_data = serializers.serialize('json', review_driver)
        return JsonResponse(json.loads(serialized_data), safe = False)

@csrf_exempt
@login_required(login_url='/authentication/login/')
def getCustomerOrder(request):
    user = request.user
    if request.method == 'GET':
        is_driver = check_user_role(user)
        if is_driver:
            return render(request, "forbidden_page.html")
        customer = Customer.objects.get(user=user)
        dashboard_customer = DashboardCustomer.objects.get(customer=customer)
        status = request.GET.get('status')

        context = {"is_driver": is_driver}
        if status == 'accepted':
            context["order"] = list(dashboard_customer.order.filter(status=OrderStatus.ACCEPTED))
            context["title"] = "Accepted Order"
        elif status == 'rejected':
            context["order"] = list(dashboard_customer.order.filter(status=OrderStatus.REJECTED))
            context["title"] = "Rejected Order"
        elif status == 'pending':
            context["order"] = list(dashboard_customer.order.filter(status=OrderStatus.PENDING))
            context["title"] = "Pending Order"
        elif status == 'finished':
            context["order"] = list(dashboard_customer.order.filter(status=OrderStatus.FINISHED))
            context["title"] = "Finished Order"

        return render(request, "dashboard_customer/index.html", context)
    return JsonResponse({"failed": "Not using GET method"}, status=405)