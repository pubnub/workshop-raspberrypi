var raspi = require('raspi-io');
var five = require('johnny-five');
var board = new five.Board({io: new raspi()});

board.on('ready', function() {

	// Create an led on pin 7 (GPIO 4) and strobe it on/off  	
  	new led = five.Led('P1-7');

  	// Optionally set the speed; Leave blank to set the default, 100ms
  	led.strobe(200);

});