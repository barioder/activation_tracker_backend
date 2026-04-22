from rest_framework import viewsets
from activation_tracker_app.controllers.merchant.update_merchant import update_merchant
from activation_tracker_app.controllers.merchant.retrieve_merchant import retrieve_merchant
from activation_tracker_app.controllers.merchant.list_merchant import list_merchant

class MerchantView(viewsets.ViewSet):
    def list(self, request):
        return list_merchant()

    def retrieve(self, request, pk=None):
        return retrieve_merchant(pk=pk)
    
    def update(self, request, pk=None):
         return update_merchant(request=request, pk=pk)

