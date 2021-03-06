from django.contrib.gis.geoip2 import GeoIP2
from .models import RequestIpInfo
from django.utils import timezone

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip


def get_ip_info(request):
	ip = get_client_ip(request)
	g = GeoIP2()
	try:
		data = g.city(ip)
	except Exception as e:
		print(e)
		data = None
	return data

def create_request_ip_info_object(data):
	if not data:
		return None
	obj = RequestIpInfo.objects.create(
		city=data.get('city'),
		country_code=data.get('country_code'),
		country_name=data.get('country_name'),
		dma_code=str(data.get('dma_code')),
		latitude=str(data.get('latitude')),
		longitude=str(data.get('longitude')),
		postal_code=data.get('postal_code'),
		region=data.get('region'),
		time_zone=data.get('time_zone')
	)
	obj.save()
	return obj


def save_request_ip_info(request):
	data = get_ip_info(request)
	if not data:
		return None
	return create_request_ip_info_object(data)
