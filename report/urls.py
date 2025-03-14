from django.urls import path
from .views import *

urlpatterns = [
	path('report/Shart', relatoriu_chart, name='relatoriu_chart'),
]