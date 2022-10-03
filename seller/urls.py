from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [ 
path('master',views.seller_master,name="master"),
path('home',views.seller_home,name="home"),  
path('about',views.seller_about,name="about"),
path('contact',views.seller_contact,name="contact"),



]