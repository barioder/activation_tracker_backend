from activation_tracker_app.models.requirement import Requirement

from rest_framework import serializers

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'