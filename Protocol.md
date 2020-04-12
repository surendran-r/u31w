The drone and the remote control app have a control channel over UDP port 50000. The drone streams the camera data over TCP port 7060. This file contains the information about the control channel data.

=U31W Drone UDP packet format=
The controller app sends UDP control packets to the drone. The drone sends back monitoring information back to the controller app. The control packers are sent continously at a constant rate with the current control information. The monitoring packets as well are sent a constant rate by the done relaying the real time monitoring information. But the rate of control information transmission is much higher than the monitoring data transmission.

==Host to drone==
The control packet send by the drone contains the information about all control's current value. The control UDP packet is made up of 11 bytes. 

* 1 byte: Header (0x66)
* 1 byte: Aliron (0x80 -> 100%, 0x00 -> 0%  , 0xFF -> 200%)
* 1 byte: Elevator (0x80 -> 100%, 0x00 -> 0%  , 0xFF -> 200%)
* 1 byte: Throttle (0x80 -> 50%, 0x00 -> 0%, 0xFF -> 100%)
* 1 byte: Rudder (0x80 -> 100%, 0x00 -> 0%  , 0xFF -> 200%)
* 1 byte: ??
* 1 byte: ??
* 1 byte: ??
* 1 byte: Flight Control bit flags 
* *  xxxxxxx0  => Normal 
* *  xxxxxxx1  => Upside Down
* *  xxxxxx0x  => Headless Off
* *  xxxxxx1x  => Headless On
* *  xxxxx0xx  => Control Off 		 
* *  xxxxx1xx  => Control On 		 
* *  xxxx0xxx  => High Speed
* *  xxxx1xxx  => Low Speed
* *  xxx1xxxx  => Take Off
* *  xx1xxxxx  => Land
* *  x1xxxxxx  => Emergency 
* 1 byte: Checksum of 2nd byte to 9th byte
* 1 byte: Trailer (0x99)

==Drone to Host==
* 1 byte: Header (0x66)
* 1 byte: Battery level (0x00 -> 0% , 0x64 -> 100%)
* 2 byte: Height
* 1 byte: ??
* 1 byte: ??
* 1 byte: Checksum of 2nd byte to 6th byte
* 1 byte: Trailer (0x99)
