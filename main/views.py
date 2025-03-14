from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users 
# from funsionariu.models import *
from ArquivoRelatoriu.models import *
from django.db.models import Sum, Count
from django.db.models import Q

@login_required()
def index(request): 
	total_sexu = Funsionario.objects.values('sexu').annotate(count=Count('id'))
	total_diresaun = Funsionario.objects.values('diresaun__name').annotate(count=Count('id'))
	total_departamentu = Funsionario.objects.values('departamentu__name').annotate(count=Count('id'))
	total_status_profisaun = Funsionario.objects.values('status_profisaun').annotate(count=Count('id'))

	# Mengirim data ke template
	context = {
		'total_sexu': total_sexu,
		'total_diresaun': total_diresaun,
		'total_departamentu': total_departamentu,
		'total_status_profisaun': total_status_profisaun,
		}

	return render(request, 'home/index.html',context)

