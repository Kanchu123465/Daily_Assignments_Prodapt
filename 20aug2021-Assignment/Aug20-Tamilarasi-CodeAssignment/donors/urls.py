from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.myRegister,name='myRegister'),
    path('search/',views.mySearch,name='mySearch'),
    path('add/',views.myDonorsPage,name='myDonorsPage'),
    path('viewall/',views.myDonorsList,name='myDonorsList'),
    path('viewdonors/<bloodgroup>',views.myDonorsDetails,name='myDonorsDetails'),
]