from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    
    path('add/',views.add_donor,name='add_doners'),
    path('search/',views.search,name='search_doners'),
    path('addapi/',views.add,name='add_doners_to_API'),
    path('all/',views.doner_list,name='all_doner_list'),
    path('update/<id>',views.doner_update,name='update_doner_details'),
    

]