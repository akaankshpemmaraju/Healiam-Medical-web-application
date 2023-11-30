from django.contrib import admin
from drugprediction.models import DrugReviewModel, PatientModel
#patient details
admin.site.register(PatientDetails)
#reviews of drugs
admin.site.register(DrugReviewModel)
admin.site.register(DrugFinalModel)
#this is admin python files.
