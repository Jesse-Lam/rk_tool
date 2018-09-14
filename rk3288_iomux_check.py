#!/usr/bin/python

import sys
import rk3288_reg
import adb_cmd
import rk3288_get_reg_val

if __name__ == "__main__":

	if adb_cmd.is_one_device() == False:
		print "There have no device or have more than one device"
		sys.exit()


	print "------------GPIO0 GPIOMUX----------"
	reg_all = rk3288_get_reg_val.GetPMUGpioIOMUX()

	for x in range(0, 3):
		reg_val = reg_all[x]
		print reg_val
		for i in range(1, 9):
			func_num = len(rk3288_reg.RK3288RegMux.GRF_GPIO0A_IOMUX[i])
			if func_num == 1:
				continue
			else:
				print rk3288_reg.RK3288RegMux.GRF_GPIO0A_IOMUX[i][0] + ':',
				if func_num == 2:
					print rk3288_reg.RK3288RegMux.GRF_GPIO0A_IOMUX[i][reg_val & 0x1]
				else:
					print rk3288_reg.RK3288RegMux.GRF_GPIO0A_IOMUX[i][reg_val & 0x3]
				reg_val = reg_val >> 2

