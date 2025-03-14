from django.contrib import admin
from .models import *

@admin.register(Funsionario)
class FunsionariAdmin(admin.ModelAdmin):
    list_display = ['nome', 'numero_identificacao', 'cargo', 'sexu', 'status']
    search_fields = ['nome', 'numero_identificacao', 'cargo']
    list_filter = ['status', 'status_profisaun']

@admin.register(KartaEntrada)
class KartaEntradaAdmin(admin.ModelAdmin):
    list_display = ['no_karta', 'assunto', 'husi', 'data_entrada']
    search_fields = ['no_karta', 'assunto', 'husi']
    list_filter = [ 'remetente']

@admin.register(KartaSaida)
class KartaSaidaAdmin(admin.ModelAdmin):
    list_display = ['no_karta', 'assunto', 'hato_o_ba', 'data_saida']
    search_fields = ['no_karta', 'assunto', 'husi']
    list_filter = ['data_saida']

@admin.register(Diresaun)
class diresaunAdmin(admin.ModelAdmin):
    list_display = ['name']
 
@admin.register(Departamentu)
class departamentoAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ArquivuRelatoriu)
class ArquivuRelatoriuAdmin(admin.ModelAdmin):
    list_display = ['titulo']

@admin.register(MapaKlinik)
class MapaKlinikAdmin(admin.ModelAdmin):
    list_display = ['naran_klinik']
    
@admin.register(ClienteRaiPoint)
class ClienteRaiPointAdmin(admin.ModelAdmin):
    list_display = ['klinika']