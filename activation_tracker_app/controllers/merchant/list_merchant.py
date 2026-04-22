from activation_tracker_app.models.merchant import Merchant
from activation_tracker_app.serializers.merchants import MerchantSerializer
from rest_framework.response import Response
from rest_framework import status

def list_merchant ():
    try:
        merchants = Merchant.objects.all()
        serializer = MerchantSerializer(merchants, many=True)
        data = {
                "status": status.HTTP_200_OK,
                'Message': 'Merchants fetched successfully',
                'data': serializer.data
                }
            
        return Response (data)
    except:
        data = {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Failed to fetch merchants'
                }
        
        return Response(data)

    
