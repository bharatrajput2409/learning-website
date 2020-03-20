from django.urls import path
from . import views

urlpatterns = [
    path('profile',views.profile, name='profile'),
    path('signin' , views.signin , name='signin'),
    path('register',views.register,name="register"),
    path('logout',views.logout,name='logout')
]