from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, renderer_classes, parser_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

import geocoder

from .models import IPv4GeoDataModel
from .utils import Metrics


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def get_ip_info(request):
    try:
        ip = request.data.get('ip', None)
        if ip:
            status = HTTP_200_OK
            ip_info = geocoder.ip(ip)
            data = {
                'result': 'success',
                'ip_info': None
            }
            if IPv4GeoDataModel.objects.filter(ipv4=ip).exists():
                ipv4_geodata = IPv4GeoDataModel.objects.get(ipv4=ip)
                data['ip_info'] = model_to_dict(ipv4_geodata)
            else:
                data['ip_info'] = {
                    "ipv4": f"{ip}",
                    "country": f"{ip_info.country}",
                    "province": f"{ip_info.province}",
                    "city": f"{ip_info.city}",
                    "latitude": f"{ip_info.latlng[0]}",
                    "longitude": f"{ip_info.latlng[1]}"
                }
                IPv4GeoDataModel.objects.create(**data['ip_info'])
        else:
            raise Exception()
    except Exception as e:
        status = HTTP_400_BAD_REQUEST
        data = {
            'result': 'error',
            'message': 'wrong value instead of valid public IPv4!'
        }
    finally:
        Metrics.count_of_api_call.inc()
        return Response(data=data, status=status)