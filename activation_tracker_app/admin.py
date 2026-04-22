from django.contrib import admin

# Register your models here.
from .models.merchant import Merchant
from .models.requirement import Requirement

admin.site.register(Merchant)
admin.site.register(Requirement)