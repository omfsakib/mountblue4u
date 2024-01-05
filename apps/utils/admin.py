from django.contrib import admin
from apps.preference.models import PreferenceModel

# Get the last PreferenceModel object or set default values
last_preference = PreferenceModel.objects.last()
site_name = last_preference.site_name if last_preference else "Mount Blue"

# Set site header, site title, and index title
admin.site.site_header = site_name
admin.site.site_title = site_name
admin.site.index_title = "Dashboard"
