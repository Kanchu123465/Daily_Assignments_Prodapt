from django.urls import path,include
from.import views
urlpatterns=[
    path('register/',views.blood_register,name='blood_register'),
    path('search/',views.blood_search,name='blood_search'),
    path('views/',views.blood_views,name='blood_views'),
    path('vi/',views.blood_vi,name='blood_vi'),
    path('single/<fetchid>',views.blood_single,name='blood_single'),
]