
    var ctx = document.getElementById('relatoriuChart').getContext('2d');
    var relatoriuChart = new Chart(ctx, {
        type: 'bar',  // Jenis grafik (bar chart)
        data: {
            labels: {{ labels|safe }},  // Tahun
            datasets: {{ datasets|safe }}  // Data per departamento
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Total Arquivu Relatoriu'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Tinan'
                    }
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                },
                title: {
                    display: true,
                    text: 'Total Arquivu Relatoriu per Departamentu per Tinan'
                }
            }
        }
    });