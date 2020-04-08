import threading
import os

try:

        time = input("please put in how fast the refresh rate is ")

	def printit():
	  threading.Timer(time, printit).start()

	  first = 'clear'
	  os.system(first)

	  second = 'vcgencmd measure_temp'
	  os.system(second)
	printit()

except KeyboardInterrupt:
	print("")
	print("quitting...")

# this scriped is for the rasberry pi and uses the "vcgencmd measure_temp" command to get cpu TEMP
# made by nosson.p.
#
