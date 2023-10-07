from django.contrib import admin

# Register your models here.
from drugprediction.models import DrugReviewModel, PatientModel

admin.site.register(DrugReviewModel)
admin.site.register(PatientModel)