/*
 * Parse the data and create a graph with the data.
 */
function parseData(fin_jScoreGraph) {
	Papa.parse("../data/live.csv", {
		download: true,
		complete: function(results) {
			fin_jScoreGraph(results.data);
		}
	});
}

function fin_jScoreGraph(data) {
	var time = [];
	var tot_jScore = ["Instantaneous Total jScore"];


	for (var i = 1; i < data.length-1; i++) {
		time.push(data[i][0]);
		tot_jScore.push(data[i][16])
	}

	console.log(time);
	//console.log(x_jerk);

	var fin_jScore_chart = c3.generate({
		bindto: '#fin_jScore_chart',
	    data: {
	        columns: [
	        	tot_jScore 
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
                max: 25,
                min: 0,
                    // Range includes padding, set 0 if no padding needed
                    // padding: {top:0, bottom:0}
            }
        },
        grid: {
            x: {
                show: true
            },
            y: {
                show: true
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

parseData(fin_jScoreGraph);

/*
window.setInterval(function() {
    parseData(fin_jScoreGraph);
}, 1000);*/
