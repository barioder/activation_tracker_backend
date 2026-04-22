from activation_tracker_app.models.requirement import Requirement
from activation_tracker_app.serializers.requirements import RequirementSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


def retrieve_requirement(pk=None):
    try:
        queryset = Requirement.objects.all()
        merchant =  get_object_or_404(queryset, pk = pk)
        serializer = RequirementSerializer(merchant)
        data = {
                "status": status.HTTP_200_OK,
                'Message': 'Requirement fetched successfully',
                'data': serializer.data
                }
        return Response (data)
    
    except:
        data = {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Failed to fetch requirement'
                }
                
        return data
