from django.db import models

# Create your models here.
class PatientData(models.Model):
    name = models.TextField(max_length=150,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    brainImage=models.ImageField(upload_to="brainImage")
    result=models.IntegerField(null=True,blank=True)