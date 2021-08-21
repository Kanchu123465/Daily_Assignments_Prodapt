from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.donor_view,name='donor_view'),
    path('add/',views.donor_create,name='donor_create'),
    path('viewall/',views.donor_list,name='donor_list'),
    path('viewdonor/<bloodgroup>',views.donor_details,name='donor_details'),
   
]