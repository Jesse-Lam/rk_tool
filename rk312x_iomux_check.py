#!/usr/bin/python

import sys
import rk312x_reg
import adb_cmd

if __name__ == "__main__":

	if adb_cmd.is_one_device() == False:
		print "There have no device or have more than one device"
		sys.exit()

#	res = adb_cmd.io_read("0x1010e000", "8")
#	if res == False:
#		print "read error"
#	else:
#		print "get the value:\n" + res

	#gpio0
	GRF_BASE = 0x20008000
	#print ('%#x'%rk312x_reg.RK312xRegMux.GRF_GPIO0A_IOMUX[0])
	addr = str(hex(GRF_BASE + rk312x_reg.RK312xRegMux.GRF_GPIO0A_IOMUX[0]))
	res = adb_cmd.io_read(addr,'16')
	print res
	witespace = ' '
	words = res.split(witespace)

	print "------------GPIO0A GPIOMUX----------"
	reg_val = int(words[2], 16)
	#print hex(reg_val)
	for i in range(1, 9):
		#print 'the length:' + str(len(rk312x_reg.RK312xRegMux.GRF_GPIO0A_IOMUX[i]))
		func_num = len(rk312x_reg.RK312xRegMux.GRF_GPIO0A_IOMUX[i])
		if func_num == 1:
			continue
		else:
			print rk312x_reg.RK312xRegMux.GRF_GPIO0A_IOMUX[i][0] + ':',
			if func_num == 2:
				print rk312x_reg.RK312xRegMux.GRF_GPIO0A_IOMUX[i][reg_val & 0x1]
			else:
				print rk312x_reg.RK312xRegMux.GRF_GPIO0A_IOMUX[i][reg_val & 0x3]
			#print hex(reg_val)
			reg_val = reg_val >> 2
			#print hex(reg_val)

	print "------------GPIO0B GPIOMUX----------"
	reg_val = int(words[3], 16)
	#print hex(reg_val)
	for i in range(1, 9):
		#print 'the length:' + str(len(rk312x_reg.RK312xRegMux.GRF_GPIO0A_IOMUX[i]))
		func_num = len(rk312x_reg.RK312xRegMux.GRF_GPIO0B_IOMUX[i])
		if func_num == 1:
			continue
		else:
			print rk312x_reg.RK312xRegMux.GRF_GPIO0B_IOMUX[i][0] + ':',
			if func_num == 2:
				print rk312x_reg.RK312xRegMux.GRF_GPIO0B_IOMUX[i][reg_val & 0x1]
			else:
				print rk312x_reg.RK312xRegMux.GRF_GPIO0B_IOMUX[i][reg_val & 0x3]
			#print hex(reg_val)
			reg_val = reg_val >> 2
			#print hex(reg_val)

