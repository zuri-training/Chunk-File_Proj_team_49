from django.urls import path
from . import views

app_name= "chunkapp"

urlpatterns = [
    path('',views.index,name='index'),#landing page url path
    path('dashboard/', views.UploadWizard.as_view(), name="dashboard"), #dashboard url path
    path('download/<str:link>', views.download_zip, name="download"), #download url
    path('faq',views.faq,name='faq'),#frequently asked questions url path
    path('recent/',views.listRecentChunks,name='recent'),#recent files url path
    path('terms and conditions/',views.termsAndConditions,name='termsandconditions'),#terms and conditions url path
    path('how_to_use',views.howTouse,name='howtouse'),#how to use url path
    path('account_settings/',views.accountSettings,name='account_settings'),#account settings url path
    path('contact_us/',views.contactUs,name='contact_us'),#contact us url path
    path('about_us/', views.about_us,name='about_us'),
    path("recent/<int:id>/delete/", views.delete_view, name="delete_chunk"),
    # path('chunksize/',views.setChunkSize,name='chunk'),
    # path('dashboard/uploadfile', views.uploadFile, name="uploadFile"),
]