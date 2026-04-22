from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from activation_tracker_app.enums.onboarding_status import ONBOARDING_STATUS_CHOICES

import uuid

class Merchant(models.Model):
  
    merchant_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    merchant_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    id_number = models.CharField(max_length=20, unique=True)

    # logic fields
    is_stuck = models.BooleanField(default=False)
    stuck_reason = models.CharField(max_length=255, null=True, blank=True)
    onboarding_status= models.CharField(max_length=20, choices=ONBOARDING_STATUS_CHOICES, default="REQUEST")

    # time stamps
    last_active = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        """returned string representation of the model"""
        return f"{self.merchant_name}  ({self.onboarding_status})"


    
