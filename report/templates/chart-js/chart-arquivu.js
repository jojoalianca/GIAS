var ctx = document.getElementById('relatoriuChart').getContext('2d');

// Data yang diterima dari backend
var labels = {{ labels|safe }}; // Tahun
var rawDatasets = {{ datasets|safe }}; // Data per departemen

// Array warna menarik untuk setiap dataset
const colors = [
    'rgba(255, 99, 132, 0.6)', // Merah
    'rgba(54, 162, 235, 0.6)', // Biru
    'rgba(75, 192, 192, 0.6)', // Hijau
    'rgba(255, 206, 86, 0.6)', // Kuning
    'rgba(153, 102, 255, 0.6)', // Ungu
    'rgba(255, 159, 64, 0.6)', // Oranye
    'rgba(199, 199, 199, 0.6)', // Abu-abu
    'rgba(83, 102, 255, 0.6)', // Biru Tua
    'rgba(40, 167, 69, 0.6)', // Hijau Tua
    'rgba(220, 53, 69, 0.6)' // Merah Tua
];

// Format datasets dengan warna menarik
var datasets = rawDatasets.map((dataset, index) => ({
    label: dataset.label, // Nama departemen
    data: dataset.data, // Data departemen
    backgroundColor: colors[index % colors.length], // Warna unik untuk setiap departemen
    borderColor: colors[index % colors.length].replace('0.6', '1'), // Border dengan opacity penuh
    borderWidth: 1
}));

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
