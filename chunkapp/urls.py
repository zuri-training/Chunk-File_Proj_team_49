from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='landingpage'),
    path('dashboard/', views.dashboard, name="dashboard"),
   
]