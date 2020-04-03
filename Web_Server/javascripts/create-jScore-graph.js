/*
 * Parse the data and create a graph with the data.
 */
function parseData(jScoreGraph) {
	Papa.parse("../data/live.csv", {
		download: true,
		complete: function(results) {
			jScoreGraph(results.data);
		}
	});
}

function jScoreGraph(data) {
	var time = [];
	var x_jScore = ["jScore X"];
	var y_jScore = ["jScore Y"];
	var z_jScore = ["jScore Z"];
	var tot_jScore = ["Total jScore"];


	for (var i = 1; i < data.length-1; i++) {
		time.push(data[i][0]);
		x_jScore.push(data[i][13]);
		y_jScore.push(data[i][14]);
		z_jScore.push(data[i][15]);
		//tot_jScore.push(data[i][16])
	}

	console.log(time);
	//console.log(x_jerk);

	var jScore_chart = c3.generate({
		bindto: '#jScore_chart',
	    data: {
	        columns: [
	        	x_jScore ,y_jScore ,z_jScore //,tot_jScore 
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
            },
            y: {
                max: 35,
                min: 0,
                    // Range includes padding, set 0 if no padding needed
                    // padding: {top:0, bottom:0}
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

parseData(jScoreGraph);

/*
window.setInterval(function() {
    parseData(jScoreGraph);
}, 1000);*/