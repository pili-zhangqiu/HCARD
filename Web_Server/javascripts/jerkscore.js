    
function parseData(jerkGraph) {
	Papa.parse("../data/live.csv", {
		download: true,
		complete: function(results) {
			jerkGraph(results.data);
		}
	});
}

function jerkGraph(data) {

//console.log(data.length)
var acc = [];
for (var i = 1; i < data.length; i++){
	acc[i-1] = []
	for (var j = 1; j < data.length; j++){
		acc[i-1][0] = data[i][1];
		acc[i-1][1] = data[i][2];
		acc[i-1][2] = data[i][3];
}
}
var vx = []
var vy = []
var vz = []
vx[0] = 0;
vy[0] = 0;
vz[0] = 0;
var dt = 0.002

for (var i = 1; i < acc.length; i++){
	vx[i] = vx[i-1] + acc[i-1][0]*dt
	vy[i] = vy[i-1] + acc[i-1][1]*dt
	vz[i] = vz[i-1] + acc[i-1][2]*dt
}

var jscorex = 0;
var jscorey = 0;
var jscorez = 0;
var jerkx = [];
var jerky = [];
var jerkz = [];


function calcJerk(acc,dt,t,xyz){
	
	if (Math.sign(acc[t][xyz])==-1) {
	var n = Math.abs(acc[t][xyz])
	}
	else{
		var n = acc[t][xyz]
	}
var lleft =  Math.pow(dt,3)
/*if (xyz == 2){
var rleftp = Math.abs(Math.min.apply(null,v))
}else{
var rleftp = Math.max.apply(Math,v)
}
var rleft = Math.pow(rleftp,2)*/
var right = n*dt
//var jerkpre = lleft/rleft
//var jerkpre = jerkpre*right
var jerkpre = lleft*right
var jerk = Math.abs((Math.log(jerkpre)))
return jerk
}

/*for (var t = 0; t < vx.length; t++){
jerkx[t] = calcJerk(acc,dt,t,0)
jerky[t] = calcJerk(acc,dt,t,1)
jerkz[t] = calcJerk(acc,dt,t,2)
*/
var t = 1;
while (t > 0){
    jerkx[t] = calcJerk(acc,dt,t,0)
    jerky[t] = calcJerk(acc,dt,t,1)
    jerkz[t] = calcJerk(acc,dt,t,2)
    t++;
if(t == 0){continue;}
jscorex = jscorex + Math.abs(jerkx[t]-jerkx[t-1])
jscorey = jscorey + Math.abs(jerky[t]-jerky[t-1])
jscorez = jscorez + Math.abs(jerkz[t]-jerkz[t-1])
}

console.log(jscorex)
console.log(jscorey)
console.log(jscorez)

//const {c3} = require("./WebGUI/javascripts/c3.min.js")
var chart = c3.generate({
	bindto: '#jerk',
	data: {
		columns: [
			jscorex,jscorey,jscorez
		]
	},
	axis: {
		x: {
			type: 'category',
			categories: t,
			tick: {
				multiline: false,
				culling: {
					max: 15
				}
			}
		}
	},
	zoom: {
		enabled: true
	},
	legend: {
		position: 'right'
	}
});
setTimeout(function(){
	window.location.reload(1);
 }, 500);
}

parseData(jerkGraph)
