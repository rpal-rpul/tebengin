from django.shortcuts import render
from authentication.models import Customer, Pengguna
from django.contrib.auth.decorators import login_required

@login_required(login_url='/authentication/login')
def home(request):
    current_user = request.user
    is_driver = check_user_role(current_user)
    try:
        profile = Pengguna.objects.filter(driver__user=current_user)[0]
    except:
        profile = Pengguna.objects.filter(customer__user=current_user)[0]
    context = {
        'user': current_user,
        'profile': profile,
        'is_driver': is_driver
    }
    
    return render(request, 'home.html', context)

def template_example(request):
    return render(request, 'template_example.html', {})

def check_user_role(user):
    is_driver = False
    try:
        Customer.objects.get(user = user)
    except:
        is_driver = True

    return is_driver