from django.db import models

# Create your models here.
class Appointment(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    date=models.DateField(max_length=255)
    time=models.TextField(max_length=255)
    age=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    address=models.TextField(max_length=255)
    message=models.TextField(max_length=255)

class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.TextField(max_length=500)

class Enquiry(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    message=models.TextField(max_length=500)