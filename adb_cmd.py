#!/usr/bin/python

import os
import subprocess

def is_one_device():
	count = 0
	cmd="adb devices"
	res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
	for i in range(len(res)-1):
		if res[i:i+len("device\n")] == "device\n":
			count+=1
	if count == 1:
		return True
	else:
		#print "there have more than one device or no device"
		return False

def io_read(addr, leng):
	cmd="adb shell io -4 -r -l " + leng + " " + addr
	#print cmd
	res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
	addr = addr[2:10] + ':'
	if res.find(addr) == 0:
		return res
	else:
		return False
		

#t = Adb()
#t.is_one_device()
#t.io_read("0x1010e000", "8")
