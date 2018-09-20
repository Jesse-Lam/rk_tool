#!/usr/bin/python
import adb_cmd
import rk3288_reg


def GetPMUGpioIOMUX():
	addr = str(hex(rk3288_reg.RK3288RegBase.PMU_BASE + 0x0084))
	res = adb_cmd.io_read(addr,'12')
	val = []
	print res
	res = res.split(' ')
	val.append(int(res[2], 16)) #PMU_GPIO0_A_IOMUX
	val.append(int(res[3], 16)) #PMU_GPIO0_B_IOMUX
	val.append(int(res[4], 16)) #PMU_GPIO0_C_IOMUX
	return val

def GetGpioIOMUX():
	addr = str(hex(rk3288_reg.RK3288RegBase.GRF_BASE + 0x000c))
	res = adb_cmd.io_read(addr,'128')
	val = []
	print res
	res = res.split('\r\n')
	for line in res:
		if line == '':
			break
		line = line.split(' ')
		#print line
		val.append(int(line[2], 16))
		val.append(int(line[3], 16))
		val.append(int(line[4], 16))
		val.append(int(line[5], 16))
	return val


#GetGpioIOMUX()
