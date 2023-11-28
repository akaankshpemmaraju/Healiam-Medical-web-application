
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from drugprediction.views import login, adddrug, postreview, getreviews, getdrugs, loaddataset, logout, getsentiment, \
    postreviewaction, viewdrug, viewreviews, patientlogin, viewsentiment, getconditions, getconditions1
urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('loginaction/',login,name='login action'),

    path('patientlogin/',TemplateView.as_view(template_name = 'patientlogin.html'),name='login'),
    path('patientloginaction/',patientlogin,name='login action'),

    path('adddrug/',TemplateView.as_view(template_name = 'adddrug.html'),name='add drug'),
    path('adddrugaction/',adddrug,name='add drug action'),

    path('postreview/',postreview,name='post review'),
    path('postreviewaction/',postreviewaction,name='post review action'),

    path('viewdrug/', viewdrug, name='view drug'),
    path('getdrugs/', getdrugs, name='get drugs'),
    

    path('getconditions/', getconditions, name='get drugs'),
    path('getconditions1/', getconditions1, name='get drugs'),

    path('viewreviews/',viewreviews,name='my reviews'),
    path('getreviews/',getreviews,name='my reviews'),

    path('viewsentiment/',viewsentiment,name='my reviews'),
    path('getsentiment/',getsentiment,name='get sentiment'),

    path('loaddataset/',loaddataset,name='load dataset'),

    path('logout/',logout,name='logout'),
]
