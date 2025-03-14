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

def PublicFilter(request):
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
