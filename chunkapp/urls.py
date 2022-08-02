from django.urls import path
from . import views

app_name= "chunkapp"

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/', views.renderDashBoardView, name="dashboard"),
    # path('dashboard/uploadfile', views.uploadFile, name="uploadFile"),
    path('faq',views.faq,name='faq'),
    path('recent/',views.listRecentChunks,name='recent'),
    path('terms and conditions/',views.termsAndConditions,name='termsandconditions'),
    path('how_to_use',views.howTouse,name='howtouse'),
    path('new/', views.UploadWizard.as_view()),
    # path('chunksize/',views.setChunkSize,name='chunk')
   
]