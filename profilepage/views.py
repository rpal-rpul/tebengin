from django.shortcuts import render, redirect, HttpResponseRedirect
from authentication.models import Pengguna,Driver,Customer
from profilepage.forms import CustomerForm, DriverForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http.response import JsonResponse
# Create your views here.


@login_required(login_url='/authentication/login')
def profile(request):
    
    profile, is_driver, is_customer = get_profile(request)
    profile.is_authenticated = True
    context = {
        'user': request.user,
        'profile': profile,
        'isdriver': is_driver,
        'iscustomer': is_customer,
    }
    return render(request, 'profilepage/profilepage.html', context)
    
@login_required(login_url='/authentication/login')
def update_data(request, *args, **kwargs):
    profile, is_driver, is_customer = get_profile(request)
    
    if request.method == 'POST':
        if is_driver:
            form = DriverForm(request.POST, request.FILES, instance=profile.driver)
        else:
            form = CustomerForm(request.POST, request.FILES, instance=profile.customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile')
        
    if is_driver:
        form = DriverForm(instance=profile.driver)
    else:
        form = CustomerForm(instance=profile.customer)
    context = {
        'form': form,
        'profile': profile,
        'isdriver': is_driver,
        'iscustomer': is_customer,
    }
    return render(request, 'profilepage/edit_data.html', context)

@login_required(login_url='/authentication/login')
def change_password(request):
    profile, is_driver, is_customer = get_profile(request)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
    form = PasswordChangeForm(user=request.user)
    response = {'form': form, 'profile': profile}
    print(response)
    return render(request, 'profilepage/change_password.html', response)

def get_profile(request):
    current_user = request.user
    # get current user's profile from polymorphic model
    try:
        profile = Pengguna.objects.filter(driver__user=current_user)[0]
        isdriver,iscustomer = True,False
    except:
        profile = Pengguna.objects.filter(customer__user=current_user)[0]
        isdriver,iscustomer = False,True
    profile.is_authenticated = True
    
    return profile, isdriver, iscustomer