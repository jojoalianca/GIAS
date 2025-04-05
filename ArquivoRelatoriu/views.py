from django.shortcuts import render,redirect,get_object_or_404 
from .models import *
from .forms import *
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from django.conf import settings

@login_required()
def pdf_list(request):
    pdfs = PDFUpload.objects.all().order_by('-uploaded_at')
    return render(request, 'info/pdf_list.html', {'pdfs': pdfs})

@login_required()   
def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')  # Ganti dengan nama URL untuk list kalau ada
    else:
        form = PDFUploadForm()
    return render(request, 'info/upload_pdf.html', {'form': form})

@login_required()
@allowed_users(allowed_roles=['admin'])
def funsionario_list(request):
	group = request.user.groups.all()[0].name
	funsionarios = Funsionario.objects.all()
	context = {
		'group':group,
		"page":"list",
		'funsionarios':funsionarios,	
	}
	return render(request, 'funsionari.html',context)


@login_required
@allowed_users(allowed_roles=['admin'])
def funsionario_create(request):
	group = request.user.groups.all()[0].name
	if request.method == "POST":
	
		form = FunsionarioForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			n = instance.nome
			instance.save()
			
			messages.success(request, f'Funsionariu {n}  aumenta ona.')
			return redirect('lista-funsionariu')
	else:	
		form = FunsionarioForm()
	context ={
		'form': form, 
		'group': group, 
		"page":"form",
		'title': 'Adisiona Funsionariu', 
	}
	return render(request, 'funsionari.html', context)

def funsionario_update(request, pk):
	funsionario = get_object_or_404(Funsionario, pk=pk)
    
	if request.method == 'POST':
		form = FunsionarioForm(request.POST, request.FILES, instance=funsionario)
		if form.is_valid():
			instance = form.save(commit=False)
			n = instance.nome
			instance.save()
			messages.success(request, f'Funsionariu {n}  Update ona.')
			return redirect('lista-funsionariu')
	else:
		form = FunsionarioForm(instance=funsionario)
	
	return render(request, 'funsionari.html', {'form': form,"page":"form", 'funsionario': funsionario})

@login_required()
@allowed_users(allowed_roles=['admin'])
def delete_Funsionariu(request, id):
	fun = get_object_or_404(Funsionario, id=id)
	an = fun.nome
	fun.delete()
	messages.warning(request, f'Funsionariu {an}  Hamos ho Susessu.')
	return redirect('lista-funsionariu')

@login_required()
@allowed_users(allowed_roles=['admin'])
def relatoriu_list(request):
	group = request.user.groups.all()[0].name
	arquivu = ArquivuRelatoriu.objects.all()
	context = {
		'group':group,
		"page":"list",
		'arquivu':arquivu,	
	}
	return render(request, 'Arquivu/arquivulist.html',context)


@login_required
@allowed_users(allowed_roles=['admin'])
def Arquivu_create(request):
	group = request.user.groups.all()[0].name
	if request.method == "POST":
	
		form = ArquivuForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			n = instance.titulo
			instance.save()
			
			messages.success(request, f'Relatori  {n}  Arquivu ona.')
			return redirect('Lista-Arquivu')
	else:	
		form = ArquivuForm()
	context ={
		'form': form, 
		'group': group, 
		"page":"form",
		'title': 'Adisiona Arquivu', 
	}
	return render(request, 'Arquivu/arquivulist.html', context)

def ArquivuRelatoriu_update(request, pk):
	arquiv = get_object_or_404(ArquivuRelatoriu, pk=pk)
    
	if request.method == 'POST':
		form = ArquivuForm(request.POST, request.FILES, instance=arquiv)
		if form.is_valid():
			instance = form.save(commit=False)
			n = instance.titulo
			instance.save()
			messages.success(request, f'Relatoriu {n}  Update ona.')
			return redirect('Lista-Arquivu')
	else:
		form = ArquivuForm(instance=arquiv)
	
	return render(request, 'Arquivu/arquivulist.html', {'form': form,"page":"form", 'arquiv': arquiv})

@login_required
def detail_ArquivuRelatoriu(request, pk):
    detalArReport = get_object_or_404(ArquivuRelatoriu, pk=pk)
    
    # Render template dengan data KartaEntrada
    return render(request, 'Arquivu/detail_detalArReport.html', {
        'detalArReport': detalArReport,
    })

@login_required()
@allowed_users(allowed_roles=['admin'])
def delete_arquivu_relatoriu(request, id):
	arquivu = get_object_or_404(ArquivuRelatoriu, id=id)
	an = arquivu.titulo
	arquivu.delete()
	messages.warning(request, f'Relatoriu ho nia Titulo {an} is Hamos ho Susessu.')
	return redirect('Lista-Arquivu')


# Karata Entrada coding
@login_required()
@allowed_users(allowed_roles=['admin'])
def kartaEntrasa_list(request):
	group = request.user.groups.all()[0].name
	entrada = KartaEntrada.objects.all()
	context = {
		'group':group,
		"page":"list",
		'entrada':entrada,	
	}
	return render(request, 'Karta/entrada.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def Entrada_create(request):
	group = request.user.groups.all()[0].name
	if request.method == "POST":
	
		form = EntradaForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			n = instance.assunto
			instance.save()
			
			messages.success(request, f'Karta Entrada ho Assuntu  {n}  Save ona.')
			return redirect('kartaEntrasa_list')
	else:	
		form = EntradaForm()
	context ={
		'form': form, 
		'group': group, 
		"page":"form",
		'title': 'Adisiona Estrada', 
	}
	return render(request, 'Karta/entrada.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def mark_as_read(request, pk):
    group = request.user.groups.all()[0].name
    # Ambil objek KartaEntrada berdasarkan primary key (pk)
    karta_entrada = get_object_or_404(KartaEntrada, pk=pk)
    
    # Jika Karta Entrada belum dibaca, tandai sebagai dibaca
    if not karta_entrada.is_read:
        karta_entrada.is_read = True
        karta_entrada.save()
    # Jika metode request adalah POST, proses form
    if request.method == 'POST':
        form = KartaEntradaForm(request.POST, request.FILES, instance=karta_entrada)
        if form.is_valid():
            form.save()
            messages.success(request, f" Karta Entrada {karta_entrada.no_karta} nia Despacho no file PDF Rai Ho Secessu.")
            return redirect('kartaEntrasa_list')  # Redirect ke halaman list Karta Entrada
    else:
        # Tampilkan form dengan instance yang sudah ada
        form = KartaEntradaForm(instance=karta_entrada)
    
    # Render template dengan form
    return render(request, 'Karta/mark_as_read_form.html', {
        'form': form,
        'group':group,
        'karta_entrada': karta_entrada,
    })

@login_required
@allowed_users(allowed_roles=['admin'])
def update_karta_entrada(request, pk):
    group = request.user.groups.all()[0].name
    karta_entrada = get_object_or_404(KartaEntrada, pk=pk)
    
    # Jika metode request adalah POST, proses form
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES, instance=karta_entrada)
        if form.is_valid():
            # Simpan perubahan ke database
            form.save()
            messages.success(request, f"Karta Entrada {karta_entrada.no_karta} atualizadu ho susesu.")
            return redirect('kartaEntrasa_list')  # Redirect ke halaman list Karta Entrada
    else:
        # Jika bukan POST, tampilkan form dengan data yang sudah ada
        form = EntradaForm(instance=karta_entrada)
    
    # Render template dengan form
    return render(request, 'Karta/entrada.html', {
        'form': form,
        'group':group,
        "page":"form",
        'karta_entrada': karta_entrada,
    })

@login_required
def detail_karta_entrada(request, pk):
    karta_entrada = get_object_or_404(KartaEntrada, pk=pk)
    
    # Render template dengan data KartaEntrada
    return render(request, 'Karta/detail_karta_entrada.html', {
        'karta_entrada': karta_entrada,
    })

@login_required()
@allowed_users(allowed_roles=['admin'])
def MapaKlinika_list(request):
	group = request.user.groups.all()[0].name
	KlinikaList = MapaKlinik.objects.all()
	context = {
		'group':group,
		"page":"list",
		'KlinikaList':KlinikaList,	
	}
	return render(request, 'mapa/klinika.html',context)
	
@login_required()
@allowed_users(allowed_roles=['admin'])
def MapaKlinikDetailView(request, pk):
    group = request.user.groups.all()[0].name
    klinika = get_object_or_404(MapaKlinik, id=pk)
    
    # Filter ClienteRaiPoint berdasarkan klinika_id
    cordinate = ClienteRaiPoint.objects.filter(klinika_id=pk)
    
    context = {
        "group": group,
        'page': "detail",
        'title': "Detalhe Klinika",
        'klinika': klinika,
        'cordinate': cordinate,  # Hanya koordinat yang terkait dengan klinik ini
    }
    return render(request, 'mapa/mapaklinik_detail.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def add_cliente_raipoint(request, klinika_id):
    # Ambil objek klinika berdasarkan klinika_id
    klinika = get_object_or_404(MapaKlinik, id=klinika_id)
    group = request.user.groups.all()[0].name

    if request.method == 'POST':
        form = ClienteRaiPointForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.klinika = klinika  # Set klinika untuk koordinat yang baru
            instance.save()
            messages.success(request, f'Kordinate ba klinika {klinika.naran_klinik} is Added Successfully.')
            return redirect('mapaklinik_detail', pk=klinika.id)
    else:
        # Inisialisasi form dengan klinika_id
        form = ClienteRaiPointForm(initial={'klinika': klinika})

    context = {
        'page': "form",
        'group': group,
        'form': form,
        'klinika': klinika,
    }
    return render(request, 'mapa/mapaklinik_detail.html', context)

@login_required()
@allowed_users(allowed_roles=['admin', 'fun', 'tsr'])
def update_cliente_raipoint(request, point_id):
    group = request.user.groups.all()[0].name
    cordinate = get_object_or_404(ClienteRaiPoint, id=point_id)  # Menggunakan nama yang lebih deskriptif

    if request.method == 'POST':
        form = ClienteRaiPointForm(request.POST, instance=cordinate)  # Hapus request.FILES jika tidak diperlukan
        if form.is_valid():
            instance = form.save()
            messages.success(request, f'Kordinate has been updated successfully.')
            return redirect('mapaklinik_detail', pk=cordinate.klinika.id)  # Perbaiki sintaks dan gunakan cordinate.klinika.id
    else:
        form = ClienteRaiPointForm(instance=cordinate)

    context = {
        "group": group,
        'page': "form",
        'title': "Atualiza Dadus",
        'form': form,
        'klinika': cordinate.klinika,  # Tambahkan klinika ke konteks jika diperlukan di template
    }
    return render(request, 'mapa/mapaklinik_detail.html', context)


@login_required()
def add_klinik(request):
    if request.method == 'POST':
        form = MapaKlinikForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('MapaKlinika_list')  # Ganti dengan URL tujuan setelah submit
    else:
        form = MapaKlinikForm()
    return render(request, 'mapa/klinika.html', {'form': form,'page':'form'})