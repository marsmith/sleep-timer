#!/usr/bin/env python

import blinkt
from datetime import datetime, time

#set time intervals, where (19,30) == 7:30pm
red_time = time(19,30)
yellow_time = time(6,15)
green_time = time(7,15)
off_time = time(9,30)

#check how current time relates to preset intervals
current_time = datetime.now().time()

#red state
if current_time >= red_time:
	blinkt.set_clear_on_exit(False)
	blinkt.set_brightness(0.1)
	blinkt.set_pixel(3, 128, 0, 0)
	blinkt.set_pixel(4, 128, 0, 0) #sets pixels 3 and 4 to red
	blinkt.show()
	print 'red state'

#yellow state
elif current_time < green_time:
	blinkt.set_clear_on_exit(False)
	blinkt.set_brightness(0.1)
	blinkt.set_pixel(3, 100, 100, 0)
	blinkt.set_pixel(4, 100, 100, 0) #sets pixels 3 and 4 to yellow
	blinkt.show()
	print 'yellow state'

#green state
elif current_time < off_time:
	blinkt.set_clear_on_exit(False)
	blinkt.set_brightness(0.2)
	blinkt.set_all(0, 128, 0) #sets all pixels to green
	blinkt.show()
	print 'green state'

#otherwise turn lights off
else:
	blinkt.set_clear_on_exit(True)
	blinkt.set_brightness(0.1)
	blinkt.set_all(0, 0, 0) #sets all pixels to off
	blinkt.show()
	print 'lights off'
