from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, renderer_classes, parser_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .models import IPv4GeoDataModel


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def get_ip_info(request):
    ip = request.data.get('ip', None)
    if ip:
        data = {
            'result': 'success',
            'ip_info': None
        }
        status = HTTP_200_OK
    else:
        data = {
            'result': 'error',
            'message': 'required filed is empty!'
        }
        status = HTTP_400_BAD_REQUEST
    return Response(data=data, status=status)