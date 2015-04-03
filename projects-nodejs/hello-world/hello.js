var pubnub = require('pubnub').init({
	publish_key : 'demo',
	subscribe_key : 'demo'
});

var channel = 'hello_world';
var message = 'Hello World from Raspberry Pi 2!';

pubnub.publish({
	channel : channel,
	message : message,
	callback : function(m) {
		var success = m[0], response = m[1];

		if (success) console.log( 'Success!', response );
		if (!success) console.log( 'Fail!', response );
	}
});