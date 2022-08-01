from django.urls import path
from . import views

app_name= "chunkapp"

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/', views.renderDashBoardView, name="dashboard"),
    path('dashboard/chunkFile', views.chunkFileView, name="chunkFile"),
    path('faq',views.faq,name='faq'),
    path('recent/',views.listRecentChunks,name='recent'),
    path('terms and conditions/',views.termsAndConditions,name='termsandconditions'),
    path('how_to_use',views.howToUse,name='howtouse'),
   
]