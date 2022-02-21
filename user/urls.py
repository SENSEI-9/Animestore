from django.urls import path
from user import views

urlpatterns =[
    path('adminlogin',views.adminlogin),
    path('adminregister',views.adminregister),
    path('admindashboard',views.admindashboard),
    path('adminedit/<int:id>',views.adminedit),
    path('adminupdate/<int:id>',views.adminupdate),
    path('admindelete/<int:id>',views.admindelete)
]