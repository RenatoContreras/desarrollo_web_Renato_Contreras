fetch("http://127.0.0.1:5000/get-estadisticas-data")
  .then((response) => response.json())
  .then((data) => {


    // gráfico Lineas

    let parsedData = data.data1.map((item) => {
      const [year, month, day] = item.fecha
        .split("-")
        .map((part) => parseInt(part, 10));
      return [
        Date.UTC(year, month - 1, day), // javascript month indices start from 0 !
        item.cantidad,
      ];
    });

    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container1"
    );

    // Update the chart with new data
    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });

    // gráfico Torta


    const data2 = data.data2.map(item => [item.tipo, item.cantidad]);

    const chart2 = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container2"
    );

    // Update the chart2 with new data
    chart2.update({
      series: [
        {
          data: data2,
        },
      ],
    });




    // OTRO

    const MMM = data.data3
    const meses = [...new Set(MMM.map(item => item.mes))].sort();

    const data_p = meses.map(mes => {
                const dato = MMM.find(item => item.mes === mes && item.tipo === 'perro');
                return dato ? dato.cantidad : 0;
            });

    const data_g = meses.map(mes => {
                const dato = MMM.find(item => item.mes === mes && item.tipo === 'gato');
                return dato ? dato.cantidad : 0;
            });

    const chart3 = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container3"
    );

    // Update the chart3 with new data
    chart3.update({
      xAxis: {
        categories: meses.map(mes => {
          const [year, month] = mes.split('-');
          return `${month}/${year}`;
        })
      },

      series: [
        {

            data: data_p,

        },
        {

            data: data_g,

        }
      ],
    });


  })
  .catch((error) => console.error("Error:", error));










// Gráfico de lineas
Highcharts.chart("container1", {
  chart: {
    type: "line",
  },
  title: {
    text: "Cantidad de Avisos de Adopción Agregados por Día",
  },
  xAxis: {
    type: "datetime",
    dateTimeLabelFormats: {
      month: "%b %e, %Y",
    },
    title: {
      text: "Fecha",
    },
  },
  yAxis: {
    title: {
      text: "Número de Avisos Creados",
    },
  },
  legend: {
    align: "left",
    verticalAlign: "top",
    borderWidth: 0,
  },

  tooltip: {
    shared: true,
    crosshairs: true,
  },

  series: [
    {
      name: "Avisos",
      data: [],
      lineWidth: 1,
      marker: {
        enabled: true,
        radius: 4,
      },
      color: "#FC2865",
    },
  ],
});



// Gráfico de torta
Highcharts.chart("container2", {
  chart: {
    type: "pie",
  },
  title: {
    text: "Cantidad Total de Avisos de Perros v/s Gatos",
  },
  xAxis: {
    type: "datetime",
    dateTimeLabelFormats: {
      month: "%b %e, %Y",
    },
    title: {
      text: "Fecha",
    },
  },
  yAxis: {
    title: {
      text: "Número de Avisos Creados",
    },
  },
  legend: {
    align: "left",
    verticalAlign: "top",
    borderWidth: 0,
  },

  tooltip: {
    shared: true,
    crosshairs: true,
  },

  series: [
    {
      name: "Avisos",
      data: [],
      lineWidth: 1,
      marker: {
        enabled: true,
        radius: 4,
      },
      color: "#FC2865",
    },
  ],
});



// Gráfico de barras
Highcharts.chart("container3", {
  chart: {
    type: "column",
  },
  title: {
    text: "Cantidad de Avisos de Agregados de Perros v/s Gatos por Meses",
  },
  xAxis: {
    // 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    categories: [],
    title: {
      text: "Meses",
    },
  },
  yAxis: {
    min: 0,
    title: {
      text: "Número de Avisos Creados",
    },
  },
  legend: {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'middle'
  },

  series: [
    {
      name: "Perros",
      data: [],
      lineWidth: 1,
      marker: {
        enabled: true,
        radius: 4,
      },
      color: "#ff0000ff",
    },
    {
      name: "Gatos",
      data: [],
      lineWidth: 1,
      marker: {
        enabled: true,
        radius: 4,
      },
      color: "#2836fcff",
    },

  ],
});
