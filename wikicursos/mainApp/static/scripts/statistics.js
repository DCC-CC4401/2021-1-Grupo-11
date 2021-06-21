function displayGraph(divId, countList, title, boundList) {
    let seriesData = [{
        name : '',
        data : countList
    }]

    console.log(countList)
    Highcharts.chart(divId, {
        chart: {
            type: 'column'
        },
        title: {
            text: "Frecuencia de: '" + title + "'"
        },
        xAxis: {
            categories: [
                boundList[0],
                '',
                '',
                '',
                boundList[1],
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
        series: seriesData
    });

}


const testData = [{
    name: '',
    data: [5, 2, 3, 4, 5]

}]


console.log(data)

const testList1 = list1
function displayGraphs() {
    for (const indicador in data) {
        displayGraph(`graph_${indicador}`, data[indicador]['count'], data[indicador]['title'], data[indicador]['bounds'])
    }
}

test = {
    xd : 3,
    hola : 'chao',
    no : 'se'

}

for (const x in test) {
    console.log(x)
    console.log(test[x])
}

for (const x of [1, 2, 3]) {
    console.log(x)
}
 

function generateStatisticsHTML() {
    
    mainDiv = document.getElementById('StatisticsColumn')   
    for (const indicador in data) { // para acceder a algún atributo se usa data[indicador][atributo]
        commentsHTML = ``
        for (const comment of data[indicador]['comment']) {  
            commentsHTML += `
                                <div class="row_flex" style="justify-content: space-around;">  
                                    <div class="globo abajo-derecha" style>${comment}</div>
                                    <img  src="/static/images/iconusercomment.png" height="70px">
                                </div>`
        }
        mainDiv.innerHTML += 
        `<div class="row_flex">
            <div class="visualization">
                <div class="encabezado">${data[indicador]["title"]}</div>
                <div style="overflow-y:scroll;">
                    <div class="row_flex">
                        <div class="graphBox">
                            <figure class="highcharts-figure">
                                <div id="graph_${indicador}"></div>
                            </figure>
                        </div>
                        <div class="column_flex"> 
                            <div class="commentBox" id="commentBox_${indicador}">
                                ${commentsHTML}
                            </div>
                            <div class='meanBar'>
                                <h2>Promedio:</h2>
                                <meter min='1' max='5' value="${data[indicador]['mean']}" low="2" high="3" optimum="4"></meter>
                                <br>
                                <div style="position:relative;">
                                    <div style="left:0; display: inline;">${data[indicador]['bounds'][0]}</div>
                                    <div style="margin-left: 60%; display: inline;">${data[indicador]['bounds'][1]}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>`
    }
}


