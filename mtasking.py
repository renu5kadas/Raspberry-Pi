import thread
import time

def print_time(threadName,delay):
    count = 0
    while True:
        time.sleep(delay)
        #count += 1
        a = time.ctime(time.time())
        mystr = threadName + ' Time:  ' + a 
        print mystr
def print_myname(threadName,delay):
    count = 0
    while True:
        time.sleep(delay)
        #count += 1
        print "\nMy new thread\n"

thread.start_new_thread(print_time, ("First Thread",2))
thread.start_new_thread(print_time, ("Second Thread",4))
thread.start_new_thread(print_myname, ("Third Thread",1.5))
while True:
    pass
