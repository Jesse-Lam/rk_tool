#!/usr/bin/python

import sys
import rk3288_reg
import adb_cmd

if __name__ == "__main__":

	if adb_cmd.is_one_device() == False:
		print "There have no device or have more than one device"
		sys.exit()
	res = adb_cmd.io_read("0x1010e000", "8")
	if res == False:
		print "read error"
	else:
		print "get the value:\n" + res
