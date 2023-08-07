from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('post/<int:pk>', views.DetailPage.as_view(), name='detail'),
    path('post/<int:pk>/delete', views.DeletePage.as_view(), name='delete'),
    path('post/<int:pk>/update', views.UpdatePage.as_view(), name='update'),
    path('post/create', views.CreatePage.as_view(), name='create'),
]