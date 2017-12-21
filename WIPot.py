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
tempgoal = 40


## This Section will grab data from the temperature sensor and print it in terminal
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

print("current temp:")
try:
    while True:
        if sensor.get_sensor_data():

            output = "C,{1:.2f} %RH".format(sensor.data.temperature)

            print(output)



if sensor.data.temperature > tempgoal: 

    inkyphat.set_border(inkyphat.BLACK)
    inkyphat.text("FRESH POTS %s" % (datetime.datetime.now().strftime(dateString)))

#inkyphat.set_rotation(180)






inkyphat.show()