from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.forms.models import model_to_dict
import json
from authentication.models import Driver
from dashboard_driver.models import Order

@csrf_exempt
def accept_order(request):
    if request.user.is_anonymous:
        return JsonResponse({"result": "Belum login"}, status=200)
    if (request.method == "POST"):
        id_order = request.POST.get("id_order")
        driver = Driver.objects.get(user = request.user)
        order_diterima = Order.objects.get(pk=id_order)
        semua_order = driver.order_set.all()

        for order in semua_order: # Alternative Flow
            if (order.status == "ACCEPTED"):
                minus_thirty = order.pickup_date - timedelta(hours = 0, minutes = 30)
                plus_thirty = order.pickup_date + timedelta(hours = 0, minutes = 30)
                if (minus_thirty <= order_diterima.pickup_date and plus_thirty >= order_diterima.pickup_date):
                    return JsonResponse({"error": "Tidak dapat menerima order! Terdapat Order yang bertabrakan."}, safe = False)

        order_diterima.status = "ACCEPTED"
        order_diterima.save()

        serialized_data = model_to_dict(order_diterima)
        return JsonResponse(serialized_data, safe = False)


@csrf_exempt
def reject_order(request):
    if request.user.is_anonymous:
        return JsonResponse({"result": "Belum login"}, status=200)
    if (request.method == "POST"):
        id_order = request.POST.get("id_order")
        order_ditolak = Order.objects.get(pk=id_order)
        order_ditolak.status = "REJECTED"
        order_ditolak.save()

        serialized_data = model_to_dict(order_ditolak)
        return JsonResponse(serialized_data, safe = False)
