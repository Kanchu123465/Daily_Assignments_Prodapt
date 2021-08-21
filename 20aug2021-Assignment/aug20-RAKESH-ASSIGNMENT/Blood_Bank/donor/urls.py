from django.urls  import path,include
from . import views
urlpatterns=[
   path('register/',views.register,name='register') ,  
   path('search/',views.search,name='search') ,  
   path('adddonor/',views.donoraddpage,name='donoraddpage') ,  
   path('viewall/',views.donor_list,name='donor_list') ,  
   path('view/<bgroup>',views.donor_details,name='donor_details') ,  
]