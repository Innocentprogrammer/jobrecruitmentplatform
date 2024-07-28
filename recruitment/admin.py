from django.contrib import admin
from recruitment.models import Recruitment

class recruitmentAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','address','gender','position','passout','experience','summary','resume')


admin.site.register(Recruitment,recruitmentAdmin)
# Register your models here.
