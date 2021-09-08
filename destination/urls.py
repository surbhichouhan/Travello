from django.urls import path
from . import views

urlpatterns = [
   
   path('dest',views.dest,name="dest")
]