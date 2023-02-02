import adafruit_bme680
import time
import board
import datetime

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

from datetime import timezone
current_GMT_timestamp = datetime.utcnow()


while True:
	print("\nTemperature: %0.1f C" % bme680.temperature)
	print("Gas: %d ohm" % bme680.gas)
	print("Humidity: %0.1f %%" %bme680.relative_humidity)
	print("Pressure: %0.3f hPa" % bme680.pressure)
	print("Altitude = %0.2f meters" % bme680.altitude)
	print (current_GMT_timestamp)
	
	time.sleep(2)
