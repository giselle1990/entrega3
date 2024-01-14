
from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('deudor/list', views.deudor_list, name="deudor_list"), 
    path('deudor/form', views.deudor_form, name="deudor_form"), 
]
