from rest_framework import routers

from activation_tracker_app.views.requirements import RequirementsView

requirement_rounter = routers.DefaultRouter()

requirement_rounter.register('requirement', RequirementsView, basename="requrement")
