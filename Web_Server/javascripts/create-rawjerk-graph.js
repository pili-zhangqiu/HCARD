/*
 * Parse the data and create a graph with the data.
 */
function parseData(jerkGraph) {
	Papa.parse("../data/live.csv", {
		download: true,
		complete: function(results) {
			jerkGraph(results.data);
		}
	});
}

function jerkGraph(data) {
	var time = [];
	var x_jerk = ["Jerk X"];
	var y_jerk = ["Jerk Y"];
	var z_jerk = ["Jerk Z"];


	for (var i = 1; i < data.length-1; i++) {
		time.push(data[i][0]);
		x_jerk.push(data[i][7]);
		y_jerk.push(data[i][8]);
		z_jerk.push(data[i][9]);
	}

	console.log(time);
	//console.log(x_jerk);

	var rawjerk_chart = c3.generate({
		bindto: '#rawjerk_chart',
	    data: {
	        columns: [
	        	x_jerk,y_jerk,z_jerk
	        ]
	    },
	    axis: {
	        x: {
	            type: 'category',
	            categories: time,
	            tick: {
                    count: 5,
                    multiline: false,
                	/*culling: {
                    	max: 4
                	}*/
            	}
	        }
	    },
	    zoom: {
        	enabled: true
    	},
	    legend: {
	        position: 'right'
		},
		datasetFill: false,
	});
}

parseData(jerkGraph);

/*
window.setInterval(function() {
    parseData(jerkGraph);
}, 1000);*/
