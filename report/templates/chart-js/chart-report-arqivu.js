document.addEventListener("DOMContentLoaded", () => {
  new ApexCharts(document.querySelector("#reportsChartFun"), {
    series: [{
      name: 'Mane',
      data: ["{% for xx in looping_funsionariu %}","{{xx.total_sexo_Mane_Dep}}","{% endfor %}"]
    }, {
      name: 'Feto',
      data: ["{% for xx in looping_funsionariu %}","{{xx.total_sexu_Feto_Dep}}","{% endfor %}"]
      }, {
      name: 'Total',
      data: ["{% for xx in looping_funsionariu %}","{{xx.total_fun}}","{% endfor %}"]
    }],
    chart: {
      height: 400,
      type: 'bar',
      toolbar: {
        show: false
      },
    },
    markers: {
      size: 12
    },
    colors: ['yellow', 'blue','red','green'],
    fill: {
      type: "gradient",
      gradient: {
        shadeIntensity: 0,
        opacityFrom: 1,
        opacityTo: 1,
        stops: [0, 90, 100]
      }
    },
    dataLabels: {
      enabled: true,
    },
    stroke: {
      curve: 'smooth',
      width: 1
    },
    xaxis: {
      type: 'text',
      categories: ["{% for ii in looping_funsionariu %}","{{ii.name}}","{% endfor %}"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    }
  }).render();
});

    