from django.urls import path
from . import views

urlpatterns = [
    path('buyer_log/', views.login, name='buyer_login'),
    path('buyer_reg/', views.register, name='buyer_register'),
    path('log_out/', views.log_out, name='buyer_logout'),
]