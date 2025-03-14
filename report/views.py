from django.shortcuts import render
from django.db.models import Count
from ArquivoRelatoriu.models import *
from collections import defaultdict

def relatoriu_chart(request):
    # Ambil semua departamento
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



    context = {
        'labels': labels,
        'datasets': datasets,
        'looping_funsionariu': ArquivuRelatoriu.objects.all(),
        'looping_funsionariu': looping_funsionariu,
        'tabular_data': tabular_data,  # Data untuk tabel
        'departamentos': list(data.keys()),  # Daftar departamento untuk header tabel
    }

    return render(request, 'relatoriu_chart.html', context)