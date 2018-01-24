import sys
## This section will add the time libraries
from PIL import ImageFont
import datetime
import time
import calendar
import icalendar
import datetime

##This line will add the inkyphat library
import inkyphat

## This line will add the bme680 breakout board library
import bme680
print("""This code will make your coffee pot an iot pot! Check at LINK TO BE ADDED SOON
for the laser cutting files)"""

dateString = "%-I:%M %p"
sensor = bme680.BME680()
tempGoal = 40
currentTemp = sensor.data.temperature
prevTemp = sensor.data.temperature



# This Section will grab data from the temperature sensor and print it in terminal on the raspberry pi
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

print("current temp:")

while True:
    if sensor.get_sensor_data(): 

        output = "{1:.2f} C".format(sensor.data.temperature)

        print(output)

''' this boolean function ensures that the temperature sensor and inkyphat will only display
the FRESH POTS on the display when the temperature is above the threshold ONCE. If a new pot is 
dropped on top of the sensor while the temperature is above the goal, nothing will change. 

If the temperature drops below the goal, it will change this to the STALE POT AVOID BRO function
ONCE.

after this, the code block will only check for a change each 5 seconds '''
    currentTemp = sensor.data.temperature
    if currentTemp > tempGoal and prevTemp < tempGoal:
        inkyphat.set_border(inkyphat.BLACK)
        inkyphat.text("FRESH POTS %s" % (datetime.datetime.now().strftime(dateString)))
        inkyphat.show()
    elif currentTemp < tempGoal and prevTemp > tempGoal:
        inkyphat.set_border(inkyphat.BLACK)
        inkyphat.clear()
        inkyphat.text("STALE POT, AVOID BRO")
        inkyphat.show()

    prevTemp = currentTemp
    time.sleep(5)
    
#inkyphat.set_rotation(180)


