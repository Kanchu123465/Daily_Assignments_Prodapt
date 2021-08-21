
from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='registration'),
    path('bloodgroup/',views.bloodgroup,name='bloodgroup'),
    path('adddonor/',views.adddonor,name='add donor'),
    path('viewdonors/',views.viewdonors,name='view all donor'),
    path('viewdetails/<bloodg>',views.viewdetails,name='view donor details'),
]
