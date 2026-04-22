from activation_tracker_app.models.requirement import Requirement
from activation_tracker_app.serializers.requirements import RequirementSerializer
from rest_framework.response import Response
from rest_framework import status

def update_requirement (request, pk=None):
        merchant =  Requirement.objects.get(pk=pk)
        serializer = RequirementSerializer(merchant, request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_200_OK,
                'message': 'Requirement updated',
                'data': serializer.data
            }
            return Response(data)
        else:
            data = {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Failed to update Requirement',
                    "error": serializer.errors
                    }
            return Response(data)
