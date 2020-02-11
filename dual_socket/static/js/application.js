ws = new WebSocket("ws://"  + location.host + '/zeromq')
ws.onopen = function(event) {
    console.log("Socket connected.");
  };
ws.onmessage = function(message) {
  payload = JSON.parse(message.data);
  console.log("ahhh")
  console.log(message.data)
  $('#latest_data').html('<h2> Data: ' + message.data + '</h2>');
};