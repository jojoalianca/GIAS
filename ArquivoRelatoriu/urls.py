from django.urls import path
from .views import *

urlpatterns = [
	path('lista/Funsionariu', funsionario_list, name="lista-funsionariu"),
	path('Adisiona/Finsionariu', funsionario_create, name='adisiona-funsionariu'),
	path('funsionario/<int:pk>/update/', funsionario_update, name='funsionario_update'),
	path('delete/<int:id>/Funsionariu/', delete_Funsionariu, name='delete_Funsionariu'),
	
	# path('phone-info-Public/<int:phone_info_id>/', phone_detail_viewPublic, name='phone_detail_viewPublic'),

	path('lista/arqiuvu', relatoriu_list, name="Lista-Arquivu"),
	path('Adisiona/arqiuvu', Arquivu_create, name="Adisiona-Arquivu"),
	path('Update/<str:pk>/arqiuvu', ArquivuRelatoriu_update, name="update-Arquivu"),
	path('delete/<int:id>/', delete_arquivu_relatoriu, name='delete_arquivu_relatoriu'),
	path('detail/arquivu/<int:pk>/report', detail_ArquivuRelatoriu, name='detail_ArquivuRelatoriu'),


	path('Lista/karta-entrada',kartaEntrasa_list, name="kartaEntrasa_list"),
	path('Adisiona/karta-entrada',Entrada_create, name="Entrada_create"),
	path('mark_as_read/<int:pk>/', mark_as_read, name='mark_as_read'),
	path('update/karta/entrada/<int:pk>/', update_karta_entrada, name='update_karta_entrada'),
	path('detail/karta_entrada/<int:pk>/', detail_karta_entrada, name='detail_karta_entrada'),


	path('Klinika/MapaKlinika/Lista ', MapaKlinika_list, name='MapaKlinika_list'),
	path('mapaklinik/<int:pk>/', MapaKlinikDetailView, name='mapaklinik_detail'),
    	path('mapaklinik/<int:klinika_id>/add_cliente_raipoint/', add_cliente_raipoint, name='add_cliente_raipoint'),
    	path('update-cliente-raipoint/<int:point_id>/', update_cliente_raipoint, name='update_cliente_raipoint'),


	]
