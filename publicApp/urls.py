from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
	path('', PublicFilter, name="index_public"),

	path('mapa-klinik/', klinik_CountMun, name='mapa_klinik'),
    path('api/klinik-data/', klinik_map_data, name='klinik_map_data'),
    path('api/klinik-summary/', klinik_summary, name='klinik_summary'),
    # path('get_municipios/', get_municipios, name='get_municipios'),

	
	]