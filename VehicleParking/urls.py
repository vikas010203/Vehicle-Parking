"""VehicleParking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from vehicle.views import *
from django.conf import settings
from django.conf.urls.static import static
from vehicle.views import profile  # Import the profile view
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
path('about',about,name='about'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs

    path('profile/', profile, name='profile'),  # Add this line for the profile view

path('contact',contact,name='contact'),
path('admin_login',admin_login,name='admin_login'),
path('admin_home',admin_home,name='admin_home'),
path('logout',Logout,name='logout'),
path('change_password',change_password,name='change_password'),
path('add_category',add_category,name='add_category'),
    path('manage_category',manage_category,name='manage_category'),
path('delete_category/<int:pid>', delete_category,name='delete_category'),
path('edit_category/<int:pid>',edit_category,name='edit_category'),
path('add_vehicle',add_vehicle,name='add_vehicle'),
path('manage_incomingvehicle',manage_incomingvehicle,name='manage_incomingvehicle'),
path('view_incomingdetail/<int:pid>',view_incomingdetail,name='view_incomingdetail'),
path('manage_outgoingvehicle',manage_outgoingvehicle,name='manage_outgoingvehicle'),
path('view_outgoingdetail/<int:pid>',view_outgoingdetail,name='view_outgoingdetail'),
    path('print/<int:pid>',print_detail,name='print'),
path('search',search,name='search'),
path('betweendate_report',betweendate_report,name='betweendate_report'),
    path('betweendate_reportdetails',betweendate_reportdetails,name='betweendate_reportdetails'),

]
