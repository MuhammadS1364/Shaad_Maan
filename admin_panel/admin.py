from django.contrib import admin

# Register your models here.
from .models import Student_info_Model, Wings_Model,Outreach_Programmes


admin.site.register(Wings_Model)
admin.site.register(Student_info_Model)
admin.site.register(Outreach_Programmes)