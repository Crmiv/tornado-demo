#!/usr/bin/env python
import threading
import time

class Consumer(threading.Thread):
	def __init__(self,t_name):
		threading.Thread.__init__(self,name=t_name)
	def run(self):
		global time
		con.acquire()
		if time > 0:
			con.wait()
		else:
			for i in range(5):
				time+=1
				print "producing---" + str(time)
			con.notify()
		print time
		con.release()

class Producer(threading.Thread):
	def __init__(self,t_name):
		threading.Thread.__init__(self,name=t_name)
	def run(self):
		global time
		con.acquire()
		if time == 0:
			
			con.wait()
		else:
			for i in range(5):
				time -= 1
				print "producing---Consumer is consuming" + str(time)
			con.notify()
		print time
		con.release()

con = threading.Condition()
time = 0
c = Consumer('con')
p = Producer('pro')
print 'aaa'
p.start()
c.start()
p.join()
c.join()

print time
		
