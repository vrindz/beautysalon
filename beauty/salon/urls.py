from django.urls import path
from . import views

urlpatterns = [

      path('', views.index,name='base'),
      path('about/', views.about, name='about'),
      path('service/', views.service, name='service'),
      path('booking', views.booking, name='booking'),
      path('contact/', views.contact, name='contact'),


]