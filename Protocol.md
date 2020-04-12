# U31W Drone WiFi communication
The drone and the remote control app have a control channel over UDP port 50000. The drone streams the camera data over TCP port 7060. This file contains the information about the control channel data.

## U31W Drone UDP packet format
The controller app sends UDP control packets to the drone. The drone sends back monitoring information back to the controller app. The control packets are sent continously at a constant rate with the current control information. The monitoring packets as well are sent a constant rate with the real time drone status information. But the rate of control information transmission is much higher than the monitoring data transmission.

### Host to drone
The control packet send by the drone contains the information about all control's current value. The control UDP packet is made up of 11 bytes. 

| Offset | Length | Value | Description | Notes |
|--------|--------|-------|-------------|-------|
| 1 | 1 byte | 0x66 | Header |
| 2 | 1 byte | 0x00 (0%) to 0xFF (200%) | Aileron (%) | Default 100% |
| 3 | 1 byte | 0x00 (0%) to 0xFF (200%) | Elevator (%) | Default 100% |
| 4 | 1 byte | 0x00 (0%) to 0xFF (100%) | Throttle (%) | Default 50% |
| 5 | 1 byte | 0x00 (0%) to 0xFF (200%) | Rudder (%) | Default 100% |
| 6 | 3 byte | 0x00 / 0x80 | Unknown (seems unused) | Default 0x80 |
| 9 | 1 byte |  | Flight Control bit flags  | See Control Flag Table |
|10 | 1 byte |  | Checksum of 2nd byte to 9th byte  | |
|11 | 1 byte | 0x99 | Trailer  | |

The following table provides the information on the bit flags used for indicating different flight modes. 

| Bit Offset | Value | Description |
|------------|-------|-------------|
| 1 | 0 | Normal Flying mode |
| 1 | 1 | Upside Down Flying mode |
| 2 | 0 | Headless Off |
| 2 | 1 | Headless On |
| 3 | 0 | Control Off |
| 3 | 1 | Control On  |
| 4 | 0 | High Speed  |
| 4 | 1 | Low Speed   |
| 5 | 1 | Trigger Auto TakeOff   |
| 6 | 1 | Trigger Auto Land   |
| 7 | 1 | Trigger Emergency Stop   |
| 8 || Unused |

### Drone to Host
The monitoring data UDP packet sent from the drone is made up of 7 bytes. The monitoring packet contains the height and the battery level information.

| Offset | Length | Value | Description |
|--------|--------|-------|-------------|
| 1 | 1 byte | 0x66 | Header |
| 2 | 1 byte | 0x00 (0) to 0x64 (100)  | Battery level (%) |
| 3 | 2 bytes| 0xFFFF (-32767) to 0x7FFF (32767) | Height (in centimeters) |
| 5 | 2 bytes| 0x00 | Unknown (atleast not used in U31W) |
| 6 | 1 byte |      | Checksum of 2nd byte to 6th byte |
| 7 | 1 byte | 0x99 | Trailer |
