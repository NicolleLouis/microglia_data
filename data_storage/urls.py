from django.urls import path

from data_storage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data_filter', views.data_filter, name='data_filter'),
    path('attribute_export', views.attribute_export, name='attribute_export'),
    path('attribute_sex_filter', views.attribute_sex_filter, name='attribute_sex_filter'),
]
