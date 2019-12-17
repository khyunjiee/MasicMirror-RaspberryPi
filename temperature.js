let {PythonShell} = require('python-shell')

PythonShell.run('temperature2.py', null, function (err) {
	if (err) throw err;
	console.log('finished');
});