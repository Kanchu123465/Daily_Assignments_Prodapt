from django.urls import path
from .import views
urlpatterns = [
    path('regi/',views.regi,name ='regi'),
    path('adddonor/',views.add,name="add"),
    path('viewall/',views.viewall,name="viewall"),
    path('search/',views.search,name='search'),
    path('view_one/<fetchid>',views.view_one,name='view_pne'),
]