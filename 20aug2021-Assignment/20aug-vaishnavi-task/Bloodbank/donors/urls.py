from . import views 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('search/',views.search,name='search'),
    path('add/',views.donor,name='donor'),
    path('all/',views.donor_list,name='donor_list'),
    path('detail/<id>',views.donordetail,name='detail'),
]
