function createPlayer(width, height, streamControl) {
  var player = new Player({
    useWorker: true,
    workerFile: "/static/js/broadway/Decoder.js",
    reuseMemory: true,
    webgl: "auto",
    size: {
      width: width,
      height: height,
    }
  });

  var frameCount = 0
  player.onPictureDecoded = function(data) {
    if (frameCount == 0) {
      console.log("First frame decoded");
    }
    frameCount++;
  };

  var container = document.getElementById("container");

  var cropDiv = document.createElement("div");
  cropDiv.style.overflow = "hidden";
  cropDiv.style.position = "absolute";
  cropDiv.style.width = width + "px";
  cropDiv.style.height = height + "px";
  
  cropDiv.appendChild(player.canvas);
  container.appendChild(cropDiv);

  var canvas = document.createElement("canvas");
  canvas.id = "overlay"
  canvas.style.position = "relative";
  canvas.width = width;
  canvas.height = height;
  container.appendChild(canvas);

  return player
}

window.onload = function() {
  protobuf.load("/static/js/messages.proto", function(err, root) {
    if (err)
      throw err;

    var ClientBound = root.lookupType("ClientBound");
    var ServerBound = root.lookupType("ServerBound")

    function streamControl(enabled) {
        serverBound = ServerBound.create({streamControl: {enabled:enabled}});
       
        socket.send(ServerBound.encode(serverBound).finish());
        // console.log(ServerBound.encode(serverBound).finish())
       
  
        
    }

    var player = null;
    var socket = new WebSocket("ws://" + window.location.host + "/stream");
    console.log(window.location.host)
    socket.binaryType = "arraybuffer";

    socket.onopen = function(event) {
      console.log("Socket connected.");
      streamControl(true);
    };

    socket.onclose = function(event) {
      console.log("Socket closed.");
    };





  });
};
