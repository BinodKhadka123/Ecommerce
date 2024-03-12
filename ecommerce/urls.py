# The views used below are normally mapped in the AdminSite instance.
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.

from django.contrib.auth import views
from django.urls import path,include

urlpatterns = [
    path("",include('ecomapps.urls')),
    path("accounts/",include("django.contrib.auth.urls")),
   
]
