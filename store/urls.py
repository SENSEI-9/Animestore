from django.urls import path
from store import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('admin',views.admin,name='admin'),
    path('signout',views.signout,name='signout'),
    path('contact',views.contact,name='contact')
    ]