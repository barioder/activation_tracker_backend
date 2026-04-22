from rest_framework import routers

from activation_tracker_app.views.merchant import MerchantView

merchant_rounter = routers.DefaultRouter()

merchant_rounter.register('merchant', MerchantView, basename="merchant")
