# This is a test program for the HC-SR501 PIR sensor.
import mcp23017_lib as MCP
import time

MCP.start(0x24)

# Connect the HC-SR501 OUT pin with the A0 pin on the MCP23017 board.
MCP.setup(16, MCP.IN, MCP.PUHIGH)

while 1:
	MCP.setup(16, MCP.IN, MCP.PUHIGH)
	if(MCP.input(16)):
		print "motion detected"
	else:
		print "no motion detected"
	time.sleep(0.5)
