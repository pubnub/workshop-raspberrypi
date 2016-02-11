/* 
 * Using a PIR motion sensor with Pi 
 * 
 */

var raspi = require('raspi-io');
var five = require('johnny-five');
var board = new five.Board({io: new raspi()});

// Initializing PubNub
var channel = 'motionsensor';
var pubnub = require('pubnub').init({
	publish_key: 'pub-c-156a6d5f-22bd-4a13-848d-b5b4d4b36695',
	subscribe_key: 'sub-c-f762fb78-2724-11e4-a4df-02ee2ddab7fe'
});

board.on('ready', function() {
	console.log('board is ready');

	// Create a new `motion` hardware instance.
	var motion = new five.IR.Motion('P1-7'); //pin 7 (GPIO 4)

	// 'calibrated' occurs once, at the beginning of a session,
	motion.on('calibrated', function() {
		console.log('calibrated');
	});

	// 'motionstart' events are fired when the 'calibrated'
	// proximal area is disrupted, generally by some form of movement
	motion.on('motionstart', function() {
		console.log('motionstart');
		pubnub.publish({
			channel: channel,
			message: 'Motion detected',
			callback: function(m) {console.log(m);}
		});
	});

	// 'motionend' events are fired following a 'motionstart' event
	// when no movement has occurred in X ms
	motion.on('motionend', function() {
		console.log('motionend');
	});
});
