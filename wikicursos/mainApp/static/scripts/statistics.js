function displayGraph(divId, data) {
    Highcharts.chart(divId, {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Título gráfico test'
        },
        xAxis: {
            categories: [
                'Muy en desacuerdo',
                'En desacuerdo',
                'Neutral',
                'De acuerdo',
                'Muy de acuerdo',
            ],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Valoraciones'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y}</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: data
    });

}


const testData = [{
    name: '',
    data: required_time_level_count // [1, 2, 3, 4, 5]

}]

const testList1 = list1
console.log(required_time_level_mean, required_time_level_count)
function displayGraphs() {
    //displayGraph('testGraph1', testData)
    displayGraph('testGraph2', testData)
    displayGraph('testGraph3', testData)
    displayGraph('testGraph4', testData)
    displayGraph('testGraph5', testData)

}