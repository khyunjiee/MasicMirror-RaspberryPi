let {PythonShell} = require('python-shell');

PythonShell.run('vibration_led.py', null, function (err) {
	if (err) throw err;
	console.log('finished');
});