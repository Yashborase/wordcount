
# from django.contrib import admin
from django.urls import path
from . import views # . dot means this directory
urlpatterns = [
	path('',views.home, name = "home"),
	path('count/', views.count, name='count')
]
