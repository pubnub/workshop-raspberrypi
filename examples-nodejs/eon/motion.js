var PUBNUB = require('pubnub');

var pubnub = PUBNUB.init({
  publish_key: 'demo',
  subscribe_key: 'demo'
});

setInterval(function(){

  pubnub.publish({
    channel: "c3-gauge-rasp-demo",
    message: {
      columns: [['data', Math.random() * 99]]
    }
  });

}, 1000);