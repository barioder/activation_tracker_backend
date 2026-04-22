from rest_framework import viewsets
from activation_tracker_app.controllers.requirement.update_requirement import update_requirement
from activation_tracker_app.controllers.requirement.retrieve_requirement import retrieve_requirement
from activation_tracker_app.controllers.requirement.list_requirement import list_requirement

class RequirementsView(viewsets.ViewSet):
    def list(self, request):
        return list_requirement()

    def retrieve(self, request, pk=None):
        return retrieve_requirement(pk=pk)
    
    def update(self, request, pk=None):
         return update_requirement(request=request, pk=pk)

