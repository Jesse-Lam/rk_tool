#!/usr/bin/python

import sys
import rk3288_reg
import adb_cmd
import rk3288_get_reg_val
import re
import os

def DisplayAllGpioMux(log):
	print >> log, "-----------RK3288 GPIO_MUX-----------"
	reg_all = rk3288_get_reg_val.GetPMUGpioIOMUX()
	for x in range(0, 3):
		reg_val = reg_all[x]
		#print hex(reg_val)
		if x == 0:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO0A_IOMUX
		if x == 1:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO0B_IOMUX
		if x == 2:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO0C_IOMUX
		for i in range(1, 9):
			func_num = len(gpio_mux[i])
			if func_num == 1:
				continue
			else:
				print >> log, gpio_mux[i][0] + ':',
				if func_num == 2:
					print >> log, gpio_mux[i][reg_val & 0x1]
				else:
					print >> log, gpio_mux[i][reg_val & 0x3]
				reg_val = reg_val >> 2
		print >> log, "-------------------------------------"


	reg_all = rk3288_get_reg_val.GetGpioIOMUX()
	for x in range(0, 25):
		#reg_val = reg_all[x]
		#print hex(reg_val)
		if x == 0:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO1D_IOMUX
		elif x == 1:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO2A_IOMUX
		elif x == 2:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO2B_IOMUX
		elif x == 3:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO2C_IOMUX
		elif x == 4:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO3A_IOMUX
		elif x == 5:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO3B_IOMUX
		elif x == 6:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO3C_IOMUX
		elif x == 7:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO3DL_IOMUX
		elif x == 8:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO3DH_IOMUX
		elif x == 9:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO4AL_IOMUX
		elif x == 10:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO4AH_IOMUX
		elif x == 11:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO4BL_IOMUX
		elif x == 12:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO4C_IOMUX
		elif x == 13:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO4D_IOMUX
		elif x == 14:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO5B_IOMUX
		elif x == 15:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO5C_IOMUX
		elif x == 16:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO6A_IOMUX
		elif x == 17:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO6B_IOMUX
		elif x == 18:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO6C_IOMUX
		elif x == 19:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO7A_IOMUX
		elif x == 20:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO7B_IOMUX
		elif x == 21:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO7CL_IOMUX
		elif x == 22:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO7CH_IOMUX
		elif x == 23:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO8A_IOMUX
		elif x == 24:
			gpio_mux = rk3288_reg.RK3288RegMux.GRF_GPIO8B_IOMUX

		reg_val_index = (gpio_mux[0] - rk3288_reg.RK3288RegMux.GRF_GPIO1D_IOMUX[0])/4
		reg_val = reg_all[reg_val_index]
		if len(gpio_mux) == 9: #for 2'b00
			for i in range(1, 9):
				func_num = len(gpio_mux[i])
				if func_num == 1:
					continue
				else:
					print >> log, gpio_mux[i][0] + ':',
					if func_num == 2:
						print >> log, gpio_mux[i][reg_val & 0x1]
					else:
						print >> log, gpio_mux[i][reg_val & 0x3]
					reg_val = reg_val >> 2
			print >> log, "-------------------------------------"
		elif len(gpio_mux) == 5: #for 3'b000
			for i in range(1, 5):
				func_num = len(gpio_mux[i])
				if func_num == 1:
					continue
				else:
					print >> log, gpio_mux[i][0] + ':',
					print >> log, gpio_mux[i][reg_val & 0x7]
					reg_val = reg_val >> 4
			print >> log, "-------------------------------------"
		elif len(gpio_mux) == 8: #for GRF_GPIO7CH_IOMUX
			print >> log, gpio_mux[1][0] + ':',
			print >> log, gpio_mux[1][reg_val & 0x3]
			reg_val = reg_val >> 2*4
			print >> log, gpio_mux[5][0] + ':',
			print >> log, gpio_mux[5][reg_val & 0x3]
			reg_val = reg_val >> 2*2
			print >> log, gpio_mux[7][0] + ':',
			print >> log, gpio_mux[7][reg_val & 0x3]
			print >> log, "-------------------------------------"

if __name__ == "__main__":

	LogFile = 'rk3288_iomux.log'

	if adb_cmd.is_one_device() == False:
		print "There have no device or have more than one device"
		sys.exit()

	if len(sys.argv) == 1:
		print "The usage:"
		print "./rk3288_iomux_check.py gpio0d0"
		print "./rk3288_iomux_check.py gpio0"
		print "./rk3288_iomux_check.py all"

	if len(sys.argv) == 2:
		#print sys.argv[1]
		if os.path.isfile(LogFile):
			os.remove(LogFile)
		f=open(LogFile,'a+')
		DisplayAllGpioMux(f);
		f.close()
		if sys.argv[1] == 'all':
			f=open(LogFile,'r')
			LogPage = f.read()
			print LogPage
			f.close()
		else:
			f=open(LogFile,'r')
			LogLines = f.readlines()
			for i in range(len(LogLines) - 1):
				if sys.argv[1] in LogLines[i]:
					print LogLines[i]
			f.close()

