# MCP23017 Library
I forked this project from ResonantWave. It is an easy to use library for the MCP23017 connected to a Raspberry Pi via IC2 bus. The picture shows the board I use for my setup.

![Board with a MCP23017 chip](https://custom-build-robots.com/wp-content/uploads/2017/03/MCP23017-300x257.jpg)

### Installation I2C

To enable the I2C support of your raspbian you have to go into the config menu and activate the I2C bus with the following command. 
```sh
$ sudo raspi-config
```
Then install the very helpful I2C tools with the following command to check the address the board is available through:

```sh
$ sudo apt-get install python-smbus i2c-tools
```
With the next command you could check under which address your MCP23017 chip is available.

```sh
pi@test:~ $ sudo i2cdetect -y 1
```
The output should look like the lines below. I changed the address from 20 to 24 by connecting pin A2 with 3.3V.
```sh
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- 24 -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
pi@test:~ $
```
### Usage

This library aims at being very similar to the RPi.GPIO library. At the moment it provides the following functions:

* `start(address)`: Starts the library on the specified chip address.

* `setup(pin, mode, pullupEnable)`: Writes direction (IN, OUT) to the specified pin. `pullupEnable` enables the internal 100k pullup resistor. Optional, and only works when setting a pin as an input. Valid values are PUHIGH and PULOW.

* `output(pin, dir)`: Writes state (HIGH, LOW) to the specified pin.

* `input(pin)`: Reads and returns pin state (True, False)

* `puRead(bank)`: Reads and returns the pullup registers from both GPIO banks.
   * Valid parameter values: **PU_A**, **PU_B**, **ALL** or leave blank for a default graphic diagram of both banks.

* `dirRead(bank)`: Reads and returns the direction registers from both GPIO banks.
   * Valid parameter values: **BANK_A**, **BANK_B**, **ALL** or leave blank for a default graphic diagram of both banks.

* `latRead(bank)`: Reads and returns the latch registers from both GPIO banks.
   * Valid parameter values: **LAT_A**, **LAT_B**, **ALL** or leave blank for a default graphic diagram of both banks.

Please refer to the image below for the pin mapping.

### Constant list

 * MCP.OUT = 1
 * MCP.IN = 0
 * MCP.BANK_A = 0
 * MCP.BANK_B = 1
 * MCP.ALL = 2
 * MCP.LAT_A = 3
 * MCP.LAT_B = 4
 * MCP.PU_A = 5
 * MCP.PU_B = 6
 * MCP.HIGH = 1
 * MCP.LOW = 0
 * MCP.PUHIGH = 1
 * MCP.PULOW = 0

### Pinout

Pins are mapped according to this diagram:

![Diagram](pinmap.png)

### Code example

This example will set pin #2 as an input, with the pullup resistor enabled and #1 as an output.
When the input goes `high`, pin #1 will also go high.

```py
import mcp23017_lib as MCP

MCP.start(0x26)

MCP.setup(2, MCP.IN, MCP.PUHIGH)
MCP.setup(1, MCP.OUT)

while 1:
   if(MCP.read(2)):
      MCP.output(1, MCP.HIGH)
   else:
      MCP.output(1, MCP.LOW)
```

### TODO list

 - [x] ~~Do not use hardcoded i2c address~~
 - [x] ~~Add pullup function~~
 - [ ] Add raw write function
 - [x] ~~Finish function documentation~~
 - [ ] GPIO Zero Support

### Contributors

Development:
 *  [@ResonantWave](https://github.com/ResonantWave)

Debugging:
 * [@rafacouto](https://github.com/rafacouto)

### Contributing

* The code is licensed under the [GPL V3](LICENSE)
* Feel free to contribute to the code
