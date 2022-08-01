from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
<<<<<<< HEAD

=======
    path('login/', views.login, name="login"),
>>>>>>> 48c98efdaa9155b2b5a56b90271c7e4435c2e842
]