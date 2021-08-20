from django.urls import path,include
from . import views
urlpatterns=[
    path('register/',views.donors,name='donors'),
    path('search/',views.search,name='search'),
    path('add/',views.donor_add,name='donor_add'),
    path('viewall/',views.donor_list,name='donor_list'),
    path('viewdonor/<fetchid>',views.donor_details,name='donor_details'),

]    