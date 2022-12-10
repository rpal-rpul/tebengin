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
from django.conf import settings
from django.conf.urls.static import static
import authentication.urls as authentication
import dashboard_driver.urls as dashboard_driver
import respons_order.urls as respons_order
import booking_driver.urls as booking_driver
<<<<<<< HEAD
<<<<<<< HEAD
=======
import profilepage.urls as profilepage
>>>>>>> c63688cbf4ac2b8bfb0bb9ea61637216ec16e189
=======
import profilepage.urls as profilepage
>>>>>>> fbf9b106606a5e733d22298a6c8ded8b21d8a993

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('authentication/', include(authentication)),
    path('dashboard-driver/', include(dashboard_driver)),
    path('respons-order/', include(respons_order)),
<<<<<<< HEAD
<<<<<<< HEAD
    path('booking-driver/', include(booking_driver))
=======
    path('booking-driver/', include(booking_driver)),
    path('profile/', include(profilepage)),
>>>>>>> c63688cbf4ac2b8bfb0bb9ea61637216ec16e189
=======
    path('booking-driver/', include(booking_driver)),
    path('profile/', include(profilepage)),
>>>>>>> fbf9b106606a5e733d22298a6c8ded8b21d8a993
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)