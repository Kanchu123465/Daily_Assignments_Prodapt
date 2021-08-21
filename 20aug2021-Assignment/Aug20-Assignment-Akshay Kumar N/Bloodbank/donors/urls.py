from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.registerDonor,name="registerDonor"),
    path('search/',views.search,name="search"),
    path('add/',views.addDonor,name="addDonor"),
    path('viewAll/',views.viewDonors,name="viewDonors"),
    path('view/<bgroup>',views.donorsData,name="donorsData"),
]