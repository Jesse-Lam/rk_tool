


class RK3288RegMux:
	GRF_GPIO0A_IOMUX	= (0x0084, \
				['gpio0a0', 'global_pwroff'], \
				['gpio0a1', 'ddrio_pwroff'], \
				['gpio0a2', 'ddr0_retention'], \
				['gpio0a3', 'ddr1_retention'], \
				['', ''], \
				['', ''], \
				['', ''], \
				['', ''])

	GRF_GPIO0B_IOMUX	= (0x0088, \
				['', ''], \
				['', ''], \
				['gpio0b2', 'tsadc_int'], \
				['', ''], \
				['', ''], \
				['gpio0b5', 'CLK_27M'], \
				['', ''], \
				['gpio0b7', 'i2c0pmu_sda'])

	GRF_GPIO0C_IOMUX	= (0x008c, \
				['gpio0c0', 'i2c0pmu_scl'], \
				['gpio0c1', 'test_clkout', 'clkt1_27m'], \
				['', ''], \
				['', ''], \
				['', ''], \
				['', ''], \
				['', ''], \
				['', ''])

	GRF_GPIO1D_IOMUX	= (0x000c, \
				['gpio1d0', 'lcdc0_hsync'], \
				['gpio1d1', 'lcdc0_vsync'], \
				['gpio1d2', 'lcdc0_den'], \
				['gpio1d3', 'lcdc0_dclk'], \
				['', ''], \
				['', ''], \
				['', ''], \
				['', ''])

	GRF_GPIO2A_IOMUX	= (0x0010, \
				['gpio2a0', 'cif_data2', 'host_din0', 'hsadc_data0'], \
				['gpio2a1', 'cif_data3', 'host_din1', 'hsadc_data1'], \
				['gpio2a2', 'cif_data4', 'host_din2', 'hsadc_data2'], \
				['gpio2a3', 'cif_data5', 'host_din3', 'hsadc_data3'], \
				['gpio2a4', 'cif_data6', 'host_ckinp', 'hsadc_data4'], \
				['gpio2a5', 'cif_data7', 'host_ckinn', 'hsadc_data5'], \
				['gpio2a6', 'cif_data8', 'host_din4', 'hsadc_data6'], \
				['gpio2a7', 'cif_data9', 'host_din5', 'hsadc_data7'])

	GRF_GPIO2B_IOMUX	=0x0014
	GRF_GPIO2C_IOMUX	=0x0018

	GRF_GPIO3A_IOMUX	=0x0020
	GRF_GPIO3B_IOMUX	=0x0024
	GRF_GPIO3C_IOMUX	=0x0028
	GRF_GPIO3DL_IOMUX	=0x002c
	GRF_GPIO3DH_IOMUX	=0x0030

	GRF_GPIO4AL_IOMUX	=0x0034
	GRF_GPIO4AH_IOMUX	=0x0038
	GRF_GPIO4BL_IOMUX	=0x003c
	GRF_GPIO4C_IOMUX	=0x0044
	GRF_GPIO4D_IOMUX	=0x0048

	GRF_GPIO5B_IOMUX	=0x0050
	GRF_GPIO5C_IOMUX	=0x0054

	GRF_GPIO6A_IOMUX	=0x005c
	GRF_GPIO6B_IOMUX	=0x0060
	GRF_GPIO6C_IOMUX	=0x0064

	GRF_GPIO7A_IOMUX	=0x006c
	GRF_GPIO7B_IOMUX	=0x0070
	GRF_GPIO7CL_IOMUX	=0x0074
	GRF_GPIO7CH_IOMUX	=0x0078

	GRF_GPIO8A_IOMUX	=0x0080
	GRF_GPIO8B_IOMUX	=0x0084

