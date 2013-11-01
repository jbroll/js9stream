

var server = require('http').Server();
var websok = require('websocket').server;
var fs     = require('fs');


ws = new websok({
      httpServer: server
    , fragmentOutgoingMessages: false
})

ws.on('request', function(request) {

    if ( request.requestedProtocols[0] != 'fits-stream' ) {
	request.reject(404, "Wrong Protocol")
    }

    var sock = request.accept('fits-stream', request.origin)

    //console.log('Conneciton Accepted')

    var count = 0

    sock.on('message', function(message) {
	//console.log('Message : ', message)

	count %= 120;
	count += 1;

	if ( message.type == "utf8" && message.utf8Data == "getimage" ) {
	    var image = "images/im." + count + ".fits"

	    //console.log(image)

	    fs.open(image, 'r',
		function(status, fd) {
		    if ( status ) { 
			//console.log("status", status)
			return;
		    }

		    stat = fs.fstatSync(fd)

		    buffer = new Buffer(stat.size)

		    fs.read(fd, buffer, 0, stat.size, 0, function() {
			fs.close(fd)
			sock.send(buffer)
		    })

		}
	    )
	}
    })
})


server.listen(3000);

