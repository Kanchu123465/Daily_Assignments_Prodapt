from . import views
from django.urls import path,include

urlpatterns = [
   
    path('register/',views.registerDonor,name='registerDonor'),
    path('search/',views.searchDonor,name='searchDonor'),
    path('adddonor/',views.add_donor_api,name='add_donor_api'),
    path('showdonors/',views.show_donor_api,name='show_donor_api'),
    path('showadonor/<bloodgroup>',views.show_a_donor_api,name='show_a_donor_api'),
]