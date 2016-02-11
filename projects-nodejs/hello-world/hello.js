var pubnub = require('pubnub').init({
	publish_key : 'pub-c-156a6d5f-22bd-4a13-848d-b5b4d4b36695',
	subscribe_key : 'sub-c-f762fb78-2724-11e4-a4df-02ee2ddab7fe'
});

var channel = 'hello-pi';

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
