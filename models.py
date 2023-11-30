from django db import models
from django db models import Model
"""
This model could be used to represent drug reviews in a Django application
where each instance of the model corresponds to a specific review with associated 
information such as the drug name condition review text and sentiment
"""
class DrugReviewModel(Model)
    drugname=models CharField(max_length=500)
    condition=models CharField(max_length=500)
    review=models CharField(max_length=5000)
    sentiment=models CharField(max_length=50)
    def __str__(self)
        return self drugname
"""
This model could be used to represent patient information in a Django application
where each instance of the model corresponds to a specific patient with associated
information such as the patient's name mobile number and prescribed drug
"""
class PatientModel(Model)

    name=models CharField(max_length=50)
    mobile=models CharField(max_length=50)
    drug=models CharField(max_length=50)
    def __str__(self)
        return self name
