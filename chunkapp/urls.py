from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.renderDashBoardView, name="dashboard"),
    path('dashboard/chunkFile', views.chunkFileView, name="chunkFile"),
   
]