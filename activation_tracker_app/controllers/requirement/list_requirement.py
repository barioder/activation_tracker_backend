from activation_tracker_app.models.requirement import Requirement
from activation_tracker_app.serializers.requirements import RequirementSerializer
from rest_framework.response import Response
from rest_framework import status

def list_requirement():
    try:
        merchants = Requirement.objects.all()
        serializer = RequirementSerializer(merchants, many=True)
        data = {
                "status": status.HTTP_200_OK,
                'Message': 'Requirements fetched successfully',
                'data': serializer.data
                }
            
        return Response (data)
    except:
        data = {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Failed to fetch requirements'
                }
        
        return Response(data)

    
