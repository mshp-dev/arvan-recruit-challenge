from django.urls import path, include
from .views import *

urlpatterns = [
    path('ip-info', get_ip_info, name='get-ip-info'),
    path('', include('django_prometheus.urls'), name='django-prometheus'),
]