from django.shortcuts import render

# Create your views here.

def save_leadcapture_email(request):
	email = request.POST.get("email")
	extra_data = request.POST.get("extra_data")
	if email:
		obj, created = LeadCaptureEmail.objects.get_or_create(email=email, extra_data=extra_data)
		if created:
			context = {
				"subject": "A new lead capture email received",
				"url": obj.get_admin_url(),
			}
			send_info_mail_to_admins(context)
			return JsonResponse({"status":"success", "msg": "Thanks for your email. We'll notify with the latest relevant stories."})
		return JsonResponse({"status":"success", "msg": "We already have your email!"})
	return JsonResponse({"status":"error", "msg": "No email provided"})
