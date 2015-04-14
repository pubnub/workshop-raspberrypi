var pubnub = require('pubnub').init({
	publish_key : 'demo',
	subscribe_key : 'demo'
});

var channel = 'hello';

var username = 'Your name';
var message = 'Hello World from Pi!';

data = {
    'username': username,
    'message': message
}

pubnub.publish({
	channel : channel,
	message : data,
	callback : function(m) {
		var success = m[0], response = m[1];

		if (success) console.log( 'Success!', response );
		if (!success) console.log( 'Fail!', response );
	}
});