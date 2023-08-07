from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name='signup'),
    path('list/', views.ListAllUsers.as_view(), name='list_users'),
]