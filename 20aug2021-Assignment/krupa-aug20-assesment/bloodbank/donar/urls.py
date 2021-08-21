from django.urls import path,include
from . import views

urlpatterns=[
    path('register/', views.register_view, name='register_view'),
    path('search/', views.search_view, name='search_view'),
    path('add/', views.adddonar, name='adddonar'),
    path('view/', views.viewdonar, name='viewdonar'),
    path('fetch/<fetchid>', views.donarupdate, name='donarupdate'),
    path('getb/<title>', views.donarget, name='donarget'),

  
]