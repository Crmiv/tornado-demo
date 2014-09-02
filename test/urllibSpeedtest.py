#!/usr/bin/env python
import urllib2
import time
import threading
import Queue

URL = ['http://www.baidu.com','http://www.sina.com','http://www.163.com']
class GetUrl(threading.Thread):
	def __init__(self):
		pass
	def run(self,_geturl):
		text = urllib2.urlopen(_geturl)
		_tst = text.read(512)
		print _tst
	
if __name__ == '__main__':
	Curtime = time.time()
	for j in range(3):
		test = GetUrl()
		test.run(URL[j])
	Fintime = time.time()
	nonfun = lambda Curtime, Fintime : (abs(Fintime - Curtime))
	print nonfun(Curtime,Fintime)

	Curtime = time.time()
	for j in range(3):
		text = urllib2.urlopen(URL[j])
		_tst = text.read(512)
		print _tst
	Fintime = time.time()
	print nonfun(Curtime,Fintime)



 
