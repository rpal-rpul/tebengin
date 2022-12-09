from django.shortcuts import render
from authentication.models import Customer

def home(request):
    profile = request.user
    is_driver = check_user_role(profile)
    context = {
        'user': profile,
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