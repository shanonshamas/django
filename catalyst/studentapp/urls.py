from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_Catalyst,name='create_catalyst'),
    path('display/',views.view_list,name='view_list'),
]