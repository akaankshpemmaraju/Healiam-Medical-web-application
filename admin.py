from django.contrib import admin
from drugprediction.models import DrugReviewModel, PatientModel

admin.site.register(DrugReviewModel)
admin.site.register(PatientModel)
