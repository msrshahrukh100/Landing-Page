from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
# Create your models here.

class RequestIpInfo(models.Model):
	city = models.CharField(max_length=255, null=True, blank=True)
	country_code = models.CharField(max_length=255, null=True, blank=True)
	country_name = models.CharField(max_length=255, null=True, blank=True)
	dma_code = models.CharField(max_length=255, null=True, blank=True)
	latitude = models.CharField(max_length=255, null=True, blank=True)
	longitude = models.CharField(max_length=255, null=True, blank=True)
	postal_code = models.CharField(max_length=255, null=True, blank=True)
	region = models.CharField(max_length=255, null=True, blank=True)
	time_zone = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return str(self.id)


class LeadCaptureEmail(models.Model):
    email = models.EmailField()
    location = models.ForeignKey(RequestIpInfo, null=True, blank=True, on_delete=models.CASCADE, related_name="location")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))
