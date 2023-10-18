from django.db import models

# Create your models here.
from django.db.models import Model


class DrugReviewModel(Model):
    drugname=models.CharField(max_length=500)
    condition=models.CharField(max_length=500)
    review=models.CharField(max_length=5000)
    sentiment=models.CharField(max_length=50)
    def __str__(self):
        return self.drugname

class PatientModel(Model):

    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    drug=models.CharField(max_length=50)
    def __str__(self):
        return self.name