var raspi = require('raspi-io');
var five = require('johnny-five');
var board = new five.Board({io: new raspi()});

board.on('ready', function() {

	// Create an led on pin 11 (GPIO 18 PCM) 
  	new led = five.Led('P1-11');

  	led.pulse();

  	// Toggle the led after 5 seconds (shown in ms)
	this.wait(5000, function() {
			led.stop().off();
		});
	});

});