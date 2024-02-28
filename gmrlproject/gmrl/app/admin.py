from django.contrib import admin
from . models import *
# Register your models here.
class Appointment_display(admin.ModelAdmin):
    list_display=['name','email','phone','date','time','age','gender','address','message']
admin.site.register(Appointment,Appointment_display)

class Contact_display(admin.ModelAdmin):
    list_display=['name','email','phone','subject','message']
admin.site.register(Contact,Contact_display)

class Enquiry_display(admin.ModelAdmin):
    list_display=['name','email','phone','message']
admin.site.register(Enquiry,Enquiry_display)