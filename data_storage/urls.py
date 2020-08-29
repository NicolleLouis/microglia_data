from django.urls import path

from data_storage.views.home import home
from data_storage.views.data_filter import data_filter
from data_storage.views.attribute_export import attribute_export
from data_storage.views.attribute_sex_filter import attribute_sex_filter
from data_storage.views.time_evolution_graph import time_evolution_graph


urlpatterns = [
    path('', home, name='home'),
    path('data_filter', data_filter, name='data_filter'),
    path('attribute_export', attribute_export, name='attribute_export'),
    path('attribute_sex_filter', attribute_sex_filter, name='attribute_sex_filter'),
    path('time_evolution_graph', time_evolution_graph, name='time_evolution_graph'),
]
