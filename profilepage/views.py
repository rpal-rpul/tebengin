from django.shortcuts import render, redirect, HttpResponseRedirect
from authentication.models import Pengguna,Driver,Customer
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http.response import JsonResponse
# Create your views here.


@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
        
    # get current user's profile from polymorphic model
    try:
        profile = Pengguna.objects.filter(driver__user=current_user)[0]
        isdriver,iscustomer = True,False
    except:
        profile = Pengguna.objects.filter(customer__user=current_user)[0]
        isdriver,iscustomer = False,True
    profile.is_authenticated = True
    context = {
        'user': current_user,
        'profile': profile,
        'isdriver': isdriver,
        'iscustomer': iscustomer,
    }

    return render(request, 'profilepage/profilepage.html', context)
    


def update_data(request):
    profile = get_profile(request)

    if request.POST.get('username') != '':
        name = request.POST.get('username')
        profile.name = name
        
    if request.POST.get('email') != '':
        email = request.POST.get('email')
        profile.email = email
    
    if request.POST.get('number') != '':
        number = request.POST.get('number')
        profile.phone_num = number
        
    profile.save()
    
    return render(request, 'profilepage/profilepage.html', {'user': profile})

@login_required(login_url='/accounts/login')
def change_password(request):
    profile = get_profile(request)
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
    try:
        profile = Pengguna.objects.filter(driver__user=current_user)[0]
    except:
        profile = Pengguna.objects.filter(customer__user=current_user)[0]
    return profile