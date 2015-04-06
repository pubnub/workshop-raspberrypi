var raspi = require('raspi-io');
var five = require('johnny-five');
var board = new five.Board({io: new raspi()});
var PUBNUB = require('pubnub');

var pubnub = PUBNUB.init({
  publish_key: 'demo',
  subscribe_key: 'demo'
});

board.on('ready', function() {

  console.log('board is ready');

  // Create a new `motion` hardware instance.
  var pin = new five.Pin({
    pin: 'P1-7'
  }); //pin 7 (GPIO 4)

  setInterval(function(){

    pin.query(function(state) {

      console.log(state)
      console.log(state.value);
      console.log(state.mode);

      pubnub.publish({
        channel: "c3-gauge-rasp-demo",
        message: {
          columns: [['data', state]]
        }
      });

    });

  }, 1000);

});

