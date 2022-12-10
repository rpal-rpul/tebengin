from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from authentication.models import Driver
from dashboard_driver.forms import AddAvailableTimeForm
from dashboard_driver.models import DashboardDriver, OrderStatus
from django.forms.models import model_to_dict
from main.views import check_user_role

@csrf_exempt
@login_required(login_url='/authentication/login/')
def addAvailableTime(request):
    user = request.user
    form = AddAvailableTimeForm(request.POST)
    is_driver = check_user_role(user)

    if not is_driver:
        return render(request, "forbidden_page.html")

    context = {
        'is_driver': is_driver,
        'form': form
    }
    driver = Driver.objects.get(user=user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            driver.available_time.add(form.instance)
            form_instance = form.instance
            available_time_begin = form_instance.available_time_begin
            available_time_end = form_instance.available_time_end

            form_instance.available_time_begin = available_time_begin.strftime("%b. %d, %Y, %I:%M %p").replace(' 0', ' ')
            form_instance.available_time_end = available_time_end.strftime("%b. %d, %Y, %I:%M %p").replace(' 0', ' ')
            form_instance.available_time_begin = form_instance.available_time_begin.replace('PM', 'p.m.')
            form_instance.available_time_begin = form_instance.available_time_begin.replace('AM', 'a.m.')
            form_instance.available_time_end = form_instance.available_time_end.replace('PM', 'p.m.')
            form_instance.available_time_end = form_instance.available_time_end.replace('AM', 'a.m.')

            context = model_to_dict(form_instance)

        elif form.errors:
            context = {
                "error_message": list(form.errors.as_data()["available_time_begin"][0])[0]
            }

        return JsonResponse(context, status=200)

    if request.method == 'GET':
        is_driver = check_user_role(request.user)
        context = {'is_driver': is_driver, 'form': form,
                   "models": driver.available_time.all()}
        return render(request, 'dashboard_driver/add_available_time.html', context, status=200)

    return JsonResponse({"failed": "Not using right method"}, status=405)


@csrf_exempt
@login_required(login_url='/authentication/login/')
def getDriverOrder(request):
    user = request.user
    if request.method == 'GET':
        is_driver = check_user_role(user)
        if not is_driver:
            return render(request, "forbidden_page.html")
        driver = Driver.objects.get(user=user)
        dashboard_driver = DashboardDriver.objects.get(driver=driver)
        status = request.GET.get('status')

        context = {"is_driver": is_driver}
        if status == 'accepted':
            context["order"] = list(dashboard_driver.order.filter(status=OrderStatus.ACCEPTED))
            context["title"] = "Accepted Order"
        elif status == 'rejected':
            context["order"] = list(dashboard_driver.order.filter(status=OrderStatus.REJECTED))
            context["title"] = "Rejected Order"
        elif status == 'pending':
            context["order"] = list(dashboard_driver.order.filter(status=OrderStatus.PENDING))
            context["title"] = "Pending Order"
            print(dashboard_driver.order.all())
        elif status == 'finished':
            context["order"] = list(dashboard_driver.order.filter(status=OrderStatus.FINISHED))
            context["title"] = "Finished Order"

        return render(request, "dashboard_driver/index.html", context)
    return JsonResponse({"failed": "Not using GET method"}, status=405)
