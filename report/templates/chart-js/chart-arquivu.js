var ctx = document.getElementById('relatoriuChart').getContext('2d');

// Data yang diterima dari backend
var labels = {{ labels|safe }}; // Tahun
var rawDatasets = {{ datasets|safe }}; // Data per departemen

// Array warna untuk setiap departemen
const colors = [
    'rgba(255, 99, 132, 0.6)', // Merah
    'rgba(54, 162, 235, 0.6)', // Biru
    'rgba(75, 192, 192, 0.6)', // Hijau
    'rgba(255, 206, 86, 0.6)', // Kuning
    'rgba(153, 102, 255, 0.6)', // Ungu
    'rgba(255, 159, 64, 0.6)' // Oranye
];

// Format datasets dengan warna
var datasets = [];
for (let i = 0; i < rawDatasets.length; i++) {
    datasets.push({
        label: rawDatasets[i].label, // Nama departemen
        data: rawDatasets[i].data, // Data departemen
        backgroundColor: colors[i % colors.length], // Warna unik untuk setiap departemen
        borderColor: colors[i % colors.length].replace('0.6', '1'), // Border dengan opacity penuh
        borderWidth: 1
    });
}

// Buat chart
var relatoriuChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: labels, // Tahun
        datasets: datasets // Data per departemen
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
