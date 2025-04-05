from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render as filtering
from django.db.models import Sum, Count
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from ArquivoRelatoriu.models import *
from django.views.generic import ListView
from django.db.models import Q
# from newsapp.models import *
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from collections import defaultdict

def PublicFilter(request):
    total_sexu = Funsionario.objects.values('sexu').annotate(count=Count('id'))
    total_diresaun = Funsionario.objects.values('diresaun__name').annotate(count=Count('id'))
    total_departamentu = Funsionario.objects.values('departamentu__name').annotate(count=Count('id'))
    total_status_profisaun = Funsionario.objects.values('status_profisaun').annotate(count=Count('id'))
    pdfs = PDFUpload.objects.all().order_by('-uploaded_at')
    departamentos = Departamentu.objects.all()

    # Buat dictionary untuk menyimpan data
    data = defaultdict(lambda: defaultdict(int))

    # Ambil semua ArquivuRelatoriu dan kelompokkan berdasarkan departamento dan tahun
    for relatoriu in ArquivuRelatoriu.objects.all():
        year = relatoriu.data_Arquivu.year
        departamento = relatoriu.departamento.name if relatoriu.departamento else "Sem Departamento"
        data[departamento][year] += 1

    # Format data untuk Chart.js
    labels = sorted(set(year for departamento in data.values() for year in departamento.keys()))
    datasets = []

    for departamento, years in data.items():
        datasets.append({
            'label': departamento,
            'data': [years.get(year, 0) for year in labels],
            'backgroundColor': f'rgba({len(departamento) * 10}, {len(departamento) * 20}, {len(departamento) * 30}, 0.2)',
            'borderColor': f'rgba({len(departamento) * 10}, {len(departamento) * 20}, {len(departamento) * 30}, 1)',
            'borderWidth': 1
        })
     # Format data untuk tabel tabular (departamento sebagai header, year sebagai baris)
    tabular_data = []
    for year in labels:
        row = {'year': year}
        for departamento in data.keys():
            row[departamento] = data[departamento].get(year, 0)
        tabular_data.append(row)

    # Debug: Cetak data ke terminal
    print("Tabular Data:", tabular_data)
    print("Departamentos:", list(data.keys()))
    print("Years:", labels)

    looping_funsionariu = []

    # Loop melalui setiap departamento
    for x in departamentos.iterator():
        total_sexo_Mane_Dep = Funsionario.objects.filter(departamentu_id=x.id, sexu="Mane").count()
        total_sexu_Feto_Dep = Funsionario.objects.filter(departamentu_id=x.id, sexu="Feto").count()
        total_fun = Funsionario.objects.filter(departamentu_id=x.id).count()

        # Tambahkan data ke list
        looping_funsionariu.append({
            'id': x.id,
            'departamento': x.name,  # Nama departamento
            'total_sexo_Mane_Dep': total_sexo_Mane_Dep,
            'total_sexu_Feto_Dep': total_sexu_Feto_Dep,
            'total_fun': total_fun,
        })
    # Mengirim data ke template
    context = {
        'total_sexu': total_sexu,
        'pdfs': pdfs,
        'total_diresaun': total_diresaun,
        'total_departamentu': total_departamentu,
        'total_status_profisaun': total_status_profisaun,
        'labels': labels,
        'datasets': datasets,
        'looping_funsionariu': ArquivuRelatoriu.objects.all(),
        'looping_funsionariu': looping_funsionariu,
        'tabular_data': tabular_data,  # Data untuk tabel
        'departamentos': list(data.keys()),  # Daftar departamento untuk header tabel
        }
    
    return render(request, 'index_public.html', context)


def klinik_map_data(request):
    clinics = ClienteRaiPoint.objects.select_related('klinika').all()
    
    data = {
        "clinics": []
    }

    for clinic in clinics:
        lat = float(clinic.latitude) if clinic.latitude else None
        lon = float(clinic.longitude) if clinic.longitude else None

        # Pastikan kita tetap menyertakan semua klinik meskipun município diisi
        data["clinics"].append({
            "name": clinic.klinika.naran_klinik,
            "type": clinic.klinika.tipo_klinik,
            "latitude": lat,
            "longitude": lon,
            "responsavel": clinic.klinika.responsavel,
            "municipality": clinic.klinika.municipality.name if clinic.klinika.municipality else "N/A",
            "image_url": clinic.image.url if clinic.image else None
        })

    return JsonResponse(data)


def klinik_summary(request):
    """
    Menghitung jumlah klinik per município berdasarkan jenisnya.
    """
    clinics = MapaKlinik.objects.all()
    summary = {}

    for clinic in clinics:
        municipality = clinic.municipality.name if clinic.municipality else "N/A"
        tipo = clinic.tipo_klinik

        if municipality not in summary:
            summary[municipality] = {"Privadu": 0, "Publiku": 0}

        if tipo in summary[municipality]:
            summary[municipality][tipo] += 1

    return JsonResponse({"summary": summary})


from django.shortcuts import render

def klinik_CountMun(request):
    """
    Menghitung jumlah klinik per município berdasarkan jenisnya.
    """
    clinics = MapaKlinik.objects.all()
    summary = {}

    for clinic in clinics:
        municipality = clinic.municipality.name if clinic.municipality else "N/A"
        tipo = clinic.tipo_klinik

        # Ensure tipo_klinik is valid
        if tipo not in ["Privadu", "Publiku"]:
            tipo = "N/A"  # In case of unexpected tipo_klinik value

        # Debugging: Print the municipality and tipo
        print(f"Municipality: {municipality}, Tipo: {tipo}")

        if municipality not in summary:
            summary[municipality] = {"Privadu": 0, "Publiku": 0}

        if tipo in summary[municipality]:
            summary[municipality][tipo] += 1

    for municipality, counts in summary.items():
        total = counts["Privadu"] + counts["Publiku"]
        counts["Total"] = total
    
    # Debugging: Print the summary dictionary
    print(f"Summary: {summary}")

    return render(request, "mapa/maps.html", {"summary": summary})
