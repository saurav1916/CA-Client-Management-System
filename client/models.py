from django.db import models

# Create your models here.
class Clientinfo(models.Model):
    name=models.CharField(max_length=100)
    pan_number=models.CharField(max_length=10)
    Return=models.FileField(blank=True)
    adhaar_number=models.CharField(max_length=20)
    contact =models.CharField(max_length=12)
    email=models.CharField(max_length=50)
    income_taxreturn=models.BooleanField(default=False)
    gst_number=models.CharField(max_length=50)