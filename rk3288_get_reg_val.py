#!/usr/bin/python
import adb_cmd
import rk3288_reg


def GetPMUGpioIOMUX():
	addr = str(hex(rk3288_reg.RK3288RegBase.PMU_BASE + 0x0084))
	res = adb_cmd.io_read(addr,'12')
	print res
	witespace = ' '
	res = res.split(witespace)
	PMU_GPIO0_A_IOMUX = int(res[2], 16)
	PMU_GPIO0_B_IOMUX = int(res[3], 16)
	PMU_GPIO0_C_IOMUX = int(res[4], 16)
	return PMU_GPIO0_A_IOMUX,PMU_GPIO0_B_IOMUX,PMU_GPIO0_C_IOMUX


val = GetPMUGpioIOMUX()
print val
