from activation_tracker_app.models.merchant import Merchant

from rest_framework import serializers


class MerchantSerializer(serializers.Serializer):
    class Meta:
        model = Merchant
        fields = '__all__'