import datetime
import csv
import sys
import argparse
import time
import RPi.GPIO as GPIO


runtime = int(sys.argv[1])
currenttime = int(time.time())
counttime = int(time.time())

#GPIO pin set up
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#variable
count = 0

# functiondefinition 
def count_p(channel):
    global count
    count += 1
    print(time.time())


GPIO.add_event_detect(26, GPIO.FALLING, callback=count_p)

meta_data = ["Time","Count"]
f = open("RadiationCount.csv","w",newline = '')
writer = csv.writer(f)
writer.writerow(meta_data)

while counttime < currenttime+runtime:
    counttime = int(time.time())
    try:
        count = 0
        time.sleep(60)
        print("CountsForCurrentMinute:", count)
    except KeyboardInterrupt: 
        GPIO.cleanup()
    data = [time.time(),count]
    writer.writerow(data)
    
f.close()
