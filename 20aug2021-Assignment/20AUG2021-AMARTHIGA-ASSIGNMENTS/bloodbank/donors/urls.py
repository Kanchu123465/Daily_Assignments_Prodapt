from django.urls import path, include
from donors import views

urlpatterns =[
    path('add/', views.adddon, name= 'adddon'),
    path('viewsingle/<fetchid>', views.details, name= 'details'),
    path('viewall/', views.viewdon, name= 'viewdon'),
    path('regdonors/', views.regdonors, name='regdonors'),
    path('search/', views.searchdonors, name='searchdonors'),
]