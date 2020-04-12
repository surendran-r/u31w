Fly See UDP packet format

Host to drone
 1 byte: Header (0x66)
 1 byte: Aliron (0x80 -> 100%, 0x00 -> 0%  , 0xFF -> 200%)
 1 byte: Elevator (0x80 -> 100%, 0x00 -> 0%  , 0xFF -> 200%)
 1 byte: Throttle (0x80 -> 50%, 0x00 -> 0%, 0xFF -> 100%)
 1 byte: Rudder (0x80 -> 100%, 0x00 -> 0%  , 0xFF -> 200%)
 1 byte: ??
 1 byte: ??
 1 byte: ??
 1 byte: Flight Control bit flags 
 		 xxxxxxx0  => Normal 
 		 xxxxxxx1  => Upside Down
		 xxxxxx0x  => Headless Off
		 xxxxxx1x  => Headless On
		 xxxxx0xx  => Control Off 		 
 		 xxxxx1xx  => Control On 		 
 		 xxxx0xxx  => High Speed
 		 xxxx1xxx  => Low Speed
 		 xxx1xxxx  => Take Off
 		 xx1xxxxx  => Land
 		 x1xxxxxx  => Emergency 
 1 byte: Checksum of 2nd byte to 9th byte
 1 byte: Trailer (0x99)


Drone to Host
 1 byte: Header (0x66)
 1 byte: Battery level (0x00 -> 0% , 0x64 -> 100%)
 2 byte: Height
 1 byte: ??
 1 byte: ??
 1 byte: Checksum of 2nd byte to 6th byte
 1 byte: Trailer (0x99)
