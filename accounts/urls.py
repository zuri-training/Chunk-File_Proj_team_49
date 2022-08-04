from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/',views.logout,name='logout'),
    path('password_change/',views.PasswordChange.as_view(),name='password_change'),
    path('password_change/done/',views.PasswordChangeDone.as_view(),name='password_change_done'),
    path('password_reset/',views.PasswordReset.as_view(),name='password_reset'),
    path('password_reset/done/',views.PasswordResetDone.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',views.PasswordResetConfirm.as_view(),name='password_reset_confirm'),
    path('reset/done/',views.PasswordResetComplete.as_view(),name='password_reset_complete'),

]