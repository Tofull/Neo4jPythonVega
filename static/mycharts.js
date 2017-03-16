// http://stackoverflow.com/questions/25129382/communication-between-python-flask-and-javascript
// setup some JSON to use
var cars = [
	{ "make":"Porsche", "model":"911S" },
	{ "make":"Mercedes-Benz", "model":"220SE" },
	{ "make":"Jaguar","model": "Mark VII" }
];

window.onload = function() {
	// setup the button click
	document.getElementById("theButton").onclick = function() {
		doWork()
	};
}

function doWork() {
	// ajax the JSON to the server
	$.post("receiver", cars, function(){

	});
	// stop link reloading the page
 event.preventDefault();
}

function makeGraphs(error, recordsJson) {
    var ctx = document.getElementById("pieChart");
          var data = {
            datasets: [{
              data: [120, 50, 140, 180, 100],
              backgroundColor: [
                "#455C73",
                "#9B59B6",
                "#BDC3C7",
                "#26B99A",
                "#3498DB"
              ],
              label: 'My dataset' // for legend
            }],
            labels: [
              "Dark Gray",
              "Purple",
              "Gray",
              "Green",
              "Blue"
            ]
          };

          var pieChart = new Chart(ctx, {
            data: data,
            type: 'pie',
            options: {
              legend: false
            }
          });
}

