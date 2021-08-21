from django.urls import path,include
from.import views
urlpatterns=[
    path("register/",views.register,name="register"),
    path("search/",views.search,name="search"),
    path("adddonar/",views.donar,name="donar"),
    path("viewdonars/",views.donarlist,name="donarlist"),
    path("viewgroup/<fetchgroup>",views.mydonars,name="mydonars"),

]