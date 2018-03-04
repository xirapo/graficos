var myctx = document.getElementById('myChart').getContext('2d');
var myctx2 = document.getElementById('Chart').getContext('2d');
var ctx = document.getElementById('myChart2').getContext('2d');
var ctx2 = document.getElementById('Chart2').getContext('2d');

var mychart = new Chart(myctx, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "My First dataset",
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [2, 10, 5, 2, 20, 30, 45],
        }]
    },

    // Configuration options go here
    options: {
        responsive: true
    }

});var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'bubble',

    // The data for our dataset
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "My First dataset",
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [{x : 2, y : 10, r : 15},
                {x : 5, y : 15, r : 15},
                {x : 1, y : 30, r : 15}]
        }]
    },

    // Configuration options go here
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    min: -30,
                    max: 30
                }
            }],
            xAxes: [{
                ticks: {
                    beginAtZero: true,
                    min: -30,
                    max: 30
                }
            }],
        },
        responsive: true,
        fill: false

    }
});

var mychart2 = new Chart(myctx2, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "My First dataset",
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [2, 10, 5, 2, 20, 30, 45],
        }]
    },

    // Configuration options go here
    options: {
        responsive: true
    }

});var chart2 = new Chart(ctx2, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "My First dataset",
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [2, 10, 5, 2, 20, 30, 45],
        }]
    },

    // Configuration options go here
    options: {
        responsive: true
    }
});
