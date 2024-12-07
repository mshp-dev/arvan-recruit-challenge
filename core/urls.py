from django.urls import path
from .views import *

urlpatterns = [
    path('ip-info', get_ip_info, name='get-ip-info'),
]