from django.urls import path,include
from . import views


urlpatterns = [
    path('register/',views.registerdonar,name='registerdonar'),
    path('search/',views.searchdonar,name='searchdonar'),
    path('add/',views.adddonar,name='adddonar'),
    path('viewall/',views.donar_list,name='donar_list'),
    path('viewone/<bloodgroup>',views.donar_details,name='donar_details'),
]