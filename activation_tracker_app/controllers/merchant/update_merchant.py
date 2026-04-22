from activation_tracker_app.models.merchant import Merchant
from activation_tracker_app.serializers.merchants import MerchantSerializer
from rest_framework.response import Response
from rest_framework import status

def update_merchant (request, pk=None):
        merchant =  Merchant.objects.get(pk=pk)
        serializer = MerchantSerializer(merchant, request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_200_OK,
                'message': 'merchant updated',
                'data': serializer.data
            }
            return Response(data)
        else:
            data = {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Failed to update merchant',
                    "error": serializer.errors
                    }
            return Response(data)
