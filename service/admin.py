from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_image','service_name','service_desc')

admin.site.register(Service,ServiceAdmin)
# Register your models here.
