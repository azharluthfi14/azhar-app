
const fixed_acidity = document.querySelector('#fixed_acidity');
const volatile_acidity = document.querySelector('#volatile_acidity');
const citric_acid = document.querySelector('#citric_acid');
const residual_sugar = document.querySelector('#residual_sugar');
const chlorides = document.querySelector('#chlorides');
const free_sulfur_dioxide = document.querySelector('#free_sulfur_dioxide');
const total_sulfur_dioxide = document.querySelector('#total_sulfur_dioxide');
const density = document.querySelector('#density');
const pH = document.querySelector('#pH');
const sulphates = document.querySelector('#sulphates');
const alcohol = document.querySelector('#alcohol');


const xtc = document.getElementById("myChart").getContext('2d');

const gradientFill = xtc.createLinearGradient(0, 0, 0, 300);
gradientFill.addColorStop(0, "rgba(255, 51,140, 1)");
gradientFill.addColorStop(1, "rgba(118, 17, 219, 0.4)");

const gradientStroke = xtc.createLinearGradient(0, 0, 0, 400);
gradientStroke.addColorStop(0, "rgba(255, 51,140, 0.5)");
gradientStroke.addColorStop(1, "rgba(0, 0, 0,0)");
let myChart = new Chart(xtc, {

    type: 'line',
    data: {
        labels: ["Fixed acidity", "Volatile acidity", "Critic acid", "Residual sugar", "Chlorides", "Free sulfur dioxide", "Total sulfur dioxide", "Density", "pH", "Sulphates", "Alcohol"],
        datasets: [{
            fill: false,
            data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            backgroundColor:
                gradientStroke
            ,
            borderColor:
                gradientFill
            ,
            pointBackgroundColor: gradientStroke,
            borderWidth: 3,
            fill: true
        }]
    },
    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            fontSize: 20,
            position: 'left',
            text: 'Statistics ',
            fontColor: '#999999'
        },
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                gridLines: {
                    color: "rgba(0, 0, 0, 0.1)",
                },
                ticks: {
                    beginAtZero: true,
                    fontColor: "#999999"
                }
            }],
            xAxes: [{
                gridLines: {
                    color: "rgba(0, 0, 0, 0.1)",
                },
                ticks: {
                    fontColor: "#999999"
                }
            }]
        }

    }
});

const updateChartValue = (input, dataOrder) => {

    input.addEventListener('change', e => {
        myChart.data.datasets[0].data[dataOrder] = e.target.value;
        myChart.update();
    });

};

updateChartValue(fixed_acidity, 0);
updateChartValue(volatile_acidity, 1);
updateChartValue(citric_acid, 2);
updateChartValue(residual_sugar, 3);
updateChartValue(chlorides, 4);
updateChartValue(free_sulfur_dioxide, 5);
updateChartValue(total_sulfur_dioxide, 6);
updateChartValue(density, 7);
updateChartValue(pH, 8);
updateChartValue(sulphates, 9);
updateChartValue(alcohol, 10);