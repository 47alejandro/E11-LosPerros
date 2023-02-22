import adafruit_bme680
import time
import board
import datetime
import busio
import csv
import argparse
import sys
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C

time.sleep(120)
print(sys.argv)

start_time = time.time()
run_time = int(sys.argv[1])
itime = start_time

n1 = datetime.now()
save = n1.strftime("%Y-%m-%d %H:%M:%S")

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

# For use with Raspberry Pi/Linux:
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25) 

# Connect to a PM2.5 sensor over UART
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, None)

# Create library object, use 'slow' 100KHz frequency!
# i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Connect to a PM2.5 sensor over I2C
# pm25 = PM25_I2C(i2c, reset_pin)
print("Found PM2.5 sensor, reading data...")
f = open("data" + save + ".csv","w", newline='')
writer = csv.writer(f)
metadata = ["PM1", "PM2.5", "PM10","Tempature", "Gas", "Humidity", "Pressure", "Altitude", "TimeinSeconds", "Time"]
writer.writerow(metadata)

while itime < (start_time + run_time):
    itime = time.time()

    time.sleep(1)

    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" %bme680.relative_humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)
    #starttime1 = time.time()

    try:
        aqdata = pm25.read()
        # print(aqdata)
        now1 = time.time()
        now = datetime.datetime.now()
        data = [aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"],bme680.temperature, bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude, now1, now]
        writer.writerow(data)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
    print()
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
    )
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
    print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
    print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
    print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
    print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
    print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
    print("---------------------------------------")
    print("Current time:")
    print(now1)
    print("---------------------------------------")
    print("Current time:")
    print(now)
f.close
