# R3-SoftwareTask2-IwanRahman

## Client and Server

The client and server works through sockets. A socket is a network end that I was able to use to establish communication
between the client and server through TCP Communication. The HOST local ip is found through a gethostname() function. 
The server binds the ip and port and listens and stores any incoming connects. Messages sent to the server from the 
client have to be decoded in byte form.

## Pynput
I used pynput to listen for any keyboard inputs. The keyboard inputs read in Keycodes, I converted to string for 
legibility and to then be able to convert that into bytes to communicate the inputs to the server. Pressing the Esc 
stops the client and server.



 
