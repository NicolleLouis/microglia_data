from django.urls import path

from data_storage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data_filter', views.data_filter, name='data_filter'),
]
