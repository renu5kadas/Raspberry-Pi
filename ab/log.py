from datetime import datetime
from time import sleep
log = open('log.txt','w')
for i in range (5):
    now=str(datetime.now())
    log.write(now + "\n")
    print(now)
    sleep(1)
log.close()
