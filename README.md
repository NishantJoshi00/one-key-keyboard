# one-key-keyboard
This is a experiment to make a keyboard using one proximity sensor and an arduino Uno. This uses the proximity sensor as a switch and then interprets its input as morse code.



## Requirements
For the hardware part the requirements are as follows:
- Arduino microcontroller
  > I have used an `Arduino Uno`
- Any device that behieves like a switch
  > I have used a `Proximity Sensor`
For the software part the requirements are as follows:
- You may require an Arduino IDE to compile the sketch and push it to the arduino board
- Python3 is required along with the pyserial library, if you don't have it just:
  ```bash
  $ pip3 install pyserial
  ```  

## Limitations
As the key interpreter uses the /dev location of the serial connection of the computer, this prototype has only been tested on a Linux box

