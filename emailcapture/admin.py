from django.contrib import admin
from .models import LeadCaptureEmail, RequestIpInfo
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

class LeadCaptureEmailResource(resources.ModelResource):
    id = Field()
    email = Field()
    city = Field()
    country_name = Field()
    time_zone = Field()
    region = Field()

    class Meta:
        model = LeadCaptureEmail

    def dehydrate_id(self, obj):
        return str(obj.id)

    def dehydrate_email(self, obj):
        return obj.email

    def dehydrate_city(self, obj):
        if obj.location:
            return obj.location.city
        return None

    def dehydrate_country_name(self, obj):
        if obj.location:
            return obj.location.country_name
        return None

    def dehydrate_time_zone(self, obj):
        if obj.location:
            return obj.location.time_zone
        return None

    def dehydrate_region(self, obj):
        if obj.location:
            return obj.location.region
        return None


# Register your models here.
class LeadCaptureEmailAdmin(ImportExportModelAdmin):
    list_display = ["email", "created_at", "updated_at", "city", "country_name", "time_zone", "region"]
    resource_class = LeadCaptureEmailResource

    def city(self, obj):
        if obj.location:
            return obj.location.city
        return None

    def country_name(self, obj):
        if obj.location:
            return obj.location.country_name
        return None

    def time_zone(self, obj):
        if obj.location:
            return obj.location.time_zone
        return None

    def region(self, obj):
        if obj.location:
            return obj.location.region
        return None

    class Meta:
        model = LeadCaptureEmail

admin.site.register(LeadCaptureEmail, LeadCaptureEmailAdmin)
admin.site.register(RequestIpInfo)
