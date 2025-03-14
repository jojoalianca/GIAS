
    // Data dari Django
    var data = {{ looping_funsionariu|safe }};

    // Siapkan data untuk ApexCharts
    var labels = data.map(item => item.departamento);
    var totalMane = data.map(item => item.total_sexo_Mane_Dep);
    var totalFeto = data.map(item => item.total_sexo_Feto_Dep);
    var totalFun = data.map(item => item.total_fun);

    // Konfigurasi chart ApexCharts
    var options = {
        chart: {
            type: 'bar',  // Jenis grafik (bar chart)
            height: 350
        },
        series: [
            {
                name: 'Total Mane',
                data: totalMane
            },
            {
                name: 'Total Feto',
                data: totalFeto
            },
            {
                name: 'Total Funsionariu',
                data: totalFun
            }
        ],
        xaxis: {
            categories: labels,  // Label untuk sumbu X (departamento)
            title: {
                text: 'Departamentu'
            }
        },
        yaxis: {
            title: {
                text: 'Total Funsionariu'
            },
            min: 0  // Mulai sumbu Y dari 0
        },
        title: {
            text: 'Total Funsionariu per Departamentu',
            align: 'center'
        },
        legend: {
            position: 'top'
        }
    };

    // Membuat grafik dengan ApexCharts
    var chart = new ApexCharts(document.querySelector("#funsionariuChart"), options);
    chart.render();
