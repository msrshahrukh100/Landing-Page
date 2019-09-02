from django.shortcuts import render
from .models import LeadCaptureEmail
from django.http import JsonResponse
from .utils import save_request_ip_info

# Create your views here.

def save_leadcapture_email(request):
    email = request.POST.get("email")
    if email:
        obj, created = LeadCaptureEmail.objects.get_or_create(email=email)
        if created:
            obj.location = save_request_ip_info(request)
            obj.save()
            return JsonResponse({"status":"success", "msg": "Thanks for your email. We'll notify with the latest relevant stories."})
        return JsonResponse({"status":"success", "msg": "We already have your email!"})
    return JsonResponse({"status":"error", "msg": "No email provided"})
