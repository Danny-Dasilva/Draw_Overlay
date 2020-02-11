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
function createPlayer1(width, height, streamControl) {
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

  var canvas = document.createElement("canvas1");
  canvas.id = "overlay"
  canvas.style.position = "relative";
  canvas.width = width;
  canvas.height = height;
  container.appendChild(canvas);

  return player
}

window.onload = function() {
  protobuf.load("/static/js/mmessages.proto", function(err, root) {
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
    var player1 = null;
    var socket = new WebSocket("ws://" + "192.168.100.2:5000" + "/stream");


    console.log(window.location.host)
    socket.binaryType = "arraybuffer";

    socket.onopen = function(event) {
      console.log("Socket connected.");
      streamControl(true);
    };

    socket.onclose = function(event) {
      console.log("Socket closed.");
    };

    socket.onmessage = function(event) {
      function buf2hex(buffer) { // buffer is an ArrayBuffer
        return Array.prototype.map.call(new Uint8Array(buffer), x => ('00' + x.toString(16)).slice(-2)).join('');
      }
      
      
      
      var x = event.data
     
      var y = x.slice(2);
      

      //console.log(y.byteLength, "1")
      if (y.byteLength > 129) {
        var y = y.slice(2)
        //  block of code to be executed if the condition is true
      } 
 
      try {
        var clientBound = ClientBound.decode(new Uint8Array(y))
        //console.log(buf2hex(y), y.byteLength, clientBound.message)
      } catch (err){
        console.log(buf2hex(y), y.byteLength, err, "error")
        

      }

      //console.log(clientBound, "CLIENT BOUN", clientBound.message)
      switch (clientBound.message) {
        
        case 'start':
          console.log('Starting...')
          start = clientBound.start;
          if (player == null) {
            console.log('Starting...')
            player = createPlayer(start.width, start.height, streamControl);
            console.log("Started: " + start.width + "x" + start.height);
          }
          if (player1 == null) {
            console.log('Starting...')
            player1 = createPlayer1(start.width, start.height, streamControl);
            console.log("Started: " + start.width + "x" + start.height);
          }
          break;
        case 'video':
          
          player.decode(clientBound.video.data);
          break;
        case 'usbvid':
          player1.decode(clientBound.usbvid.data);
          break;
        case 'stop':
          console.log("Stopped.");
          break;
      }
    }


    });
  };

