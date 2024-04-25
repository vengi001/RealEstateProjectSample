from django.contrib import admin

from REP_App.models import property_profile, tenant_profile

# Register your models here.
admin.site.register(property_profile)
admin.site.register(tenant_profile)
