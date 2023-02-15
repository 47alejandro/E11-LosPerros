import random
import time
import argparse
import sys

print(sys.argv)

start_time = time.time()
run_time = int(sys.argv[1])
itime = start_time

while itime < (start_time + run_time):
    itime = time.time()
    idata = random.random()
    print(itime, idata)
    time.sleep(1)