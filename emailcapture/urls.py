from django.urls import path
from .views import save_leadcapture_email

urlpatterns = [
    path('save-leadcapture-email/', save_leadcapture_email, name="save_leadcapture_email"),
]
