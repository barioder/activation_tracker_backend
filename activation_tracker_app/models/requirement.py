from django.db import models
from .merchant import Merchant
from enums.document_type import TYPE_CHOICES
from enums.document_status import STATUS_CHOICES
from utils.requirement.save_requirement import save_requirement
from utils.requirement.update_parent_merchant import update_parent_merchant
import uuid


class Requirement (models.Model):
    requirement_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='requirements')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PENDING')
    requirement_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    comment = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # auto update of status field before saving
        save_requirement(self)
    
        super().save(*args, **kwargs)

        # update of parent merchant model onboarding status 
        update_parent_merchant(self)

    # returns a string representation of the model
    def __str__(self):
        return f"{self.merchant.merchant_name} - {self.requirement_type} - {self.status}" 

