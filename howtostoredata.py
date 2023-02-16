import time
itime = time.time
print time
temp = 24.5
hum = 35.4
presure = 1017.2
gas = 89450
print(itime, temp, hum, press, gas)

data= [itime, temp, hum, press, gas]
f = open [data.csv, w]
meta_data = ["Time", "temp", "hum", "press", "gas"]

import csv
f = open ("data.csv" ,"w")
writer = csv.writer(f)
writer.writerow(meta_data)
writer.writerow(data)
f.close