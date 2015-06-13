'''
Created on Oct 17, 2014

@author: khiemtd
'''
#!/usr/bin/python 
 
import thread, threading
import time 
 
# Define a function for the thread 
def print_timeq(threadName, delay):
    count = 0 
    while count < 2: 
        time.sleep(delay) 
        count += 1 
        print "%s: %s" % ( threadName, time.ctime(time.time()) ) 
 
# Create two threads as follows 
#===============================================================================
# try: 
#    thread.start_new_thread( print_timeq, ("Thread-1", 2, ) ) 
#    thread.start_new_thread( print_timeq, ("Thread-2", 4, ) )
#    print threading.activeCount() 
# except: 
#    print "Error: unable to start thread" 
#  
# while 1: 
#    pass 
#===============================================================================

#!/usr/bin/python 
 
import threading 
import time 
 
exitFlag = 0 
 
class myThread (threading.Thread): 
    def __init__(self, threadID, name, counter): 
        threading.Thread.__init__(self) 
        self.threadID = threadID 
        self.name = name 
        self.counter = counter# delay time 
    def run(self): 
        print "Starting " + self.name 
        print_time(self.name, self.counter, 5) #5 >> so lan chay
        print "Exiting " + self.name 
 
def print_time(threadName, delay, counter): 
    while counter:   #run 5 lan
        #if exitFlag: 
        #    thread.exit() 
        time.sleep(delay) 
        print "%s: %s" % (threadName, time.ctime(time.time())) 
        counter -= 1 
 
# Create new threads 
thread1 = myThread(1, "Thread-1", 1) 
thread2 = myThread(2, "Thread-2", 2) 
# Start new Threads 
#thread1.start() 
#thread2.start() 
 
print "Exiting Main Thread"

"spawn threads until you type 'q'"
import thread
def child(tid):
    print 'hello thread',tid
def parent():
    i = 0
    while True:
        i += 1
        thread.start_new_thread(child, (i,))
        if input() == 'q': break
parent()


