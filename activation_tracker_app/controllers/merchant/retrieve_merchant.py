from activation_tracker_app.models.merchant import Merchant
from activation_tracker_app.serializers.merchants import MerchantSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


def retrieve_merchant(pk=None):
    try:
        queryset = Merchant.objects.all()
        merchant =  get_object_or_404(queryset, pk = pk)
        serializer = MerchantSerializer(merchant)
        data = {
                "status": status.HTTP_200_OK,
                'Message': 'Merchant fetched successfully',
                'data': serializer.data
                }
        return Response (data)
    
    except:
        data = {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Failed to fetch merchants'
                }
                
        return data
