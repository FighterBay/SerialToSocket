# SerialToSocket
Reads data from Serial(Arduino?) port and forwards it to socket.
You could probably port forward on the server and could potentially send data from a serial device over a network to another computer.

This was reliably used for having telemetry over Internet.
Tested on Pixhawk w/ Raspberry Pi to transmit telemetry over 10km(As long as both the client and server are connected).
