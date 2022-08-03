from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('password_change/',views.PasswordChange.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done'),
    path('password_reset/',views.PasswordReset.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',views.PasswordResetConfirm.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_complete.html'),)

]