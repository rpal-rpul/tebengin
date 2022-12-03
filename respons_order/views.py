from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from django.forms.models import model_to_dict
import json
from dashboard_driver.models import Order

@csrf_exempt
def accept_order(request):
    if (request.method == "POST"):
        id_order = request.POST.get("id_order")
        order_diterima = Order.objects.get(pk=id_order)
        order_diterima.status = "ACCEPTED"
        order_diterima.pickup_date = datetime.now()
        order_diterima.save()


        serialized_data = model_to_dict(order_diterima)
        return JsonResponse(serialized_data, safe = False)


@csrf_exempt
def reject_order(request):
    if (request.method == "POST"):
        id_order = request.POST.get("id_order")
        order_ditolak = Order.objects.get(pk=id_order)
        order_ditolak.status = "REJECTED"
        order_ditolak.pickup_date = datetime.now()
        order_ditolak.save()

        serialized_data = model_to_dict(order_ditolak)
        return JsonResponse(serialized_data, safe = False)
