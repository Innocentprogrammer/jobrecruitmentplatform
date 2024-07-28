from django.contrib import admin
from internship.models import Internship

class InternshipAdmin(admin.ModelAdmin):
    list_display=('job_image','job_name','job_desc')

admin.site.register(Internship, InternshipAdmin)
# Register your models here.
