from django.db import models

# Create your models here.
class LeadCaptureEmail(models.Model):
	email = models.EmailField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.email

	def get_admin_url(self):
		content_type = ContentType.objects.get_for_model(self.__class__)
		return settings.BASE_URL + reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))
