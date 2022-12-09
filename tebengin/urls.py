"""tebengin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import authentication.urls as authentication
import dashboard_driver.urls as dashboard_driver
import respons_order.urls as respons_order
import booking_driver.urls as booking_driver
<<<<<<< HEAD
=======
import profilepage.urls as profilepage
>>>>>>> c63688cbf4ac2b8bfb0bb9ea61637216ec16e189

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('authentication/', include(authentication)),
    path('dashboard-driver/', include(dashboard_driver)),
    path('respons-order/', include(respons_order)),
<<<<<<< HEAD
    path('booking-driver/', include(booking_driver))
=======
    path('booking-driver/', include(booking_driver)),
    path('profile/', include(profilepage)),
>>>>>>> c63688cbf4ac2b8bfb0bb9ea61637216ec16e189
]
