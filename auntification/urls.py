from django.urls import path
from . import views

urlpatterns = [
        path('register/', views.register, name='register'),
        path('login/', views.login_system, name='login'),
        path('logout/',views.logout_system, name='logout')
]