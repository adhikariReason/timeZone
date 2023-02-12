// import data from './data.json' assert {type:'JSON'}
// import json from JSON
document.getElementById('time-display').onclick = function(){
	console.log('Clicked')
	// let json = require('./data.json');
	// console.log(json, 'the json obj');
	let fr = new FileReader();
	document.getElementById('time-display').innerHTML = fr.readAsText(this.files[0])

}