import os
import time

with open('data.txt', 'r', os.O_NONBLOCK) as f:
    for line_terminated in f:
        line = line_terminated.rstrip('\n')
        time.sleep(5)
        print line
         #content = f.readlines()
         #content = [x.strip() for x in content]
         #print x.strip()
        