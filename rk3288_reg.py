

class RK3288RegBase:
	PMU_BASE	=0xff730000
	GRF_BASE	=0xff770000

class RK3288RegMux:

				# 2'b00
	GRF_GPIO0A_IOMUX	= (0x0084, \
				['gpio0a0', 'global_pwroff'], \
				['gpio0a1', 'ddrio_pwroff'], \
				['gpio0a2', 'ddr0_retention'], \
				['gpio0a3', 'ddr1_retention'], \
				[''], \
				[''], \
				[''], \
				[''])

				# 2'b00
	GRF_GPIO0B_IOMUX	= (0x0088, \
				[''], \
				[''], \
				['gpio0b2', 'tsadc_int'], \
				[''], \
				[''], \
				['gpio0b5', 'CLK_27M'], \
				[''], \
				['gpio0b7', 'i2c0pmu_sda'])

				# 2'b00
	GRF_GPIO0C_IOMUX	= (0x008c, \
				['gpio0c0', 'i2c0pmu_scl'], \
				['gpio0c1', 'test_clkout', 'clkt1_27m'], \
				[''], \
				[''], \
				[''], \
				[''], \
				[''], \
				[''])

				# 2'b00
	GRF_GPIO1D_IOMUX	= (0x000c, \
				['gpio1d0', 'lcdc0_hsync'], \
				['gpio1d1', 'lcdc0_vsync'], \
				['gpio1d2', 'lcdc0_den'], \
				['gpio1d3', 'lcdc0_dclk'], \
				[''], \
				[''], \
				[''], \
				[''])

				# 2'b00
	GRF_GPIO2A_IOMUX	= (0x0010, \
				['gpio2a0', 'cif_data2', 'host_din0', 'hsadc_data0'], \
				['gpio2a1', 'cif_data3', 'host_din1', 'hsadc_data1'], \
				['gpio2a2', 'cif_data4', 'host_din2', 'hsadc_data2'], \
				['gpio2a3', 'cif_data5', 'host_din3', 'hsadc_data3'], \
				['gpio2a4', 'cif_data6', 'host_ckinp', 'hsadc_data4'], \
				['gpio2a5', 'cif_data7', 'host_ckinn', 'hsadc_data5'], \
				['gpio2a6', 'cif_data8', 'host_din4', 'hsadc_data6'], \
				['gpio2a7', 'cif_data9', 'host_din5', 'hsadc_data7'])

				# 2'b00
	GRF_GPIO2B_IOMUX	= (0x0014, \
				['gpio2b0', 'cif_vsync', 'host_din6', 'hsadcts_sync'], \
				['gpio2b1', 'cif_href', 'host_din7', 'hsadcts_valid'], \
				['gpio2b2', 'cif_clkin', 'host_wkack', 'gps_clk'], \
				['gpio2b3', 'cif_clkout', 'host_wkreq', 'hsadcts_fail'], \
				['gpio2b4', 'cif_data0'], \
				['gpio2b5', 'cif_data1'], \
				['gpio2b6', 'cif_data10'], \
				['gpio2b7', 'cif_data11'])

				# 2'b00
	GRF_GPIO2C_IOMUX	= (0x0018, \
				['gpio2c0', 'i2c3cam_scl'], \
				['gpio2c1', 'i2c3cam_sda'], \
				[''], \
				[''], \
				[''], \
				[''], \
				[''], \
				[''])

				# 2'b00
	GRF_GPIO3A_IOMUX	= (0x0020, \
				['gpio3a0', 'flash0_data0', 'emmc_data0', 'reserved'], \
				['gpio3a1', 'flash0_data1', 'emmc_data1', 'reserved'], \
				['gpio3a2', 'flash0_data2', 'emmc_data2', 'reserved'], \
				['gpio3a3', 'flash0_data3', 'emmc_data3', 'reserved'], \
				['gpio3a4', 'flash0_data4', 'emmc_data4', 'reserved'], \
				['gpio3a5', 'flash0_data5', 'emmc_data5', 'reserved'], \
				['gpio3a6', 'flash0_data6', 'emmc_data6', 'reserved'], \
				['gpio3a7', 'flash0_data7', 'emmc_data7', 'reserved'])

				# 2'b00
	GRF_GPIO3B_IOMUX	= (0x0024, \
				['gpio3b0', 'flash0_rdy'], \
				['gpio3b1', 'flash0_wp', 'emmc_pwren', 'reserved'], \
				['gpio3b2', 'flash0_rdn'], \
				['gpio3b3', 'flash0_ale'], \
				['gpio3b4', 'flash0_cle'], \
				['gpio3b5', 'flash0_wrn'], \
				['gpio3b6', 'flash0_csn0'], \
				['gpio3b7', 'flash0_csn1'])

				# 2'b00
	GRF_GPIO3C_IOMUX	= (0x0028, \
				['gpio3c0', 'flash0_csn2', 'emmc_cmd', 'reserved'], \
				['gpio3c1', 'flash0_csn3', 'emmc_rstnout', 'reserved'], \
				['gpio3c2', 'flash0_dqs', 'emmc_clkout', 'reserved'], \
				[''], \
				[''], \
				[''], \
				[''], \
				[''])

				# 3'b000
	GRF_GPIO3DL_IOMUX	= (0x002c, \
				['gpio3d0', 'flash1_data0', 'host_dout0', 'mac_txd2', 'sdio1_data0'], \
				['gpio3d1', 'flash1_data1', 'host_dout1', 'mac_txd3', 'sdio1_data1'], \
				['gpio3d2', 'flash1_data2', 'host_dout2', 'mac_rxd2', 'sdio1_data2'], \
				['gpio3d3', 'flash1_data3', 'host_dout3', 'mac_rxd3', 'sdio1_data3'],)

				# 3'b000
	GRF_GPIO3DH_IOMUX	= (0x0030, \
				['gpio3d4', 'flash1_data4', 'host_dout4', 'mac_txd0', 'sdio1_detectn'], \
				['gpio3d5', 'flash1_data5', 'host_dout5', 'mac_txd1', 'sdio1_wrprt'], \
				['gpio3d6', 'flash1_data6', 'host_dout6', 'mac_rxd0', 'sdio1_bkpwr'], \
				['gpio3d7', 'flash1_data7', 'host_dout7', 'mac_rxd1', 'sdio1_intn'])

				# 3'b000
	GRF_GPIO4AL_IOMUX	= (0x0034, \
				['gpio4a0', 'flash1_rdy', 'host_ckoutp', 'mac_mdc'], \
				['gpio4a1', 'flash1_wp', 'host_ckoutn', 'mac_rxdv', 'flash0_csn4'], \
				['gpio4a2', 'flash1_rdn', 'host_dout8', 'mac_rxer', 'flash0_csn5'], \
				['gpio4a3', 'flash1_ale', 'host_dout9', 'mac_clk', 'flash0_csn6'])

				# 3'b000
	GRF_GPIO4AH_IOMUX	= (0x0038, \
				['gpio4a4', 'flash1_cle', 'host_dout10', 'mac_txen', 'flash0_csn7'], \
				['gpio4a5', 'flash1_wrn', 'host_dout11', 'mac_mdio'], \
				['gpio4a6', 'flash1_csn0', 'host_dout12', 'mac_rxclk', 'sdio1_cmd'], \
				['gpio4a7', 'flash1_csn1', 'host_dout13', 'mac_crs', 'sdio1_clkout'])

				# 3'b000
	GRF_GPIO4BL_IOMUX	= (0x003c, \
				['gpio4b0', 'flash1_dqs', 'host_dout14', 'mac_col', 'flash1_csn3'], \
				['gpio4b1', 'flash1_csn2', 'host_dout15', 'mac_txclk', 'sdio1_pwren'], \
				[''], \
				[''])

				# 2'b00
	GRF_GPIO4C_IOMUX	= (0x0044, \
				['gpio4c0', 'uart0bt_sin'], \
				['gpio4c1', 'uart0bt_sout'], \
				['gpio4c2', 'uart0bt_ctsn'], \
				['gpio4c3', 'uart0bt_rtsn'], \
				['gpio4c4', 'sdio0_data0'], \
				['gpio4c5', 'sdio0_data1'], \
				['gpio4c6', 'sdio0_data2'], \
				['gpio4c7', 'sdio0_data3'])

				# 2'b00
	GRF_GPIO4D_IOMUX	= (0x0048, \
				['gpio4d0', 'sdio0_cmd'], \
				['gpio4d1', 'sdio0_clkout'], \
				['gpio4d2', 'sdio0_detectn'], \
				['gpio4d3', 'sdio0_wrprt'], \
				['gpio4d4', 'sdio0_pwren'], \
				['gpio4d5', 'sdio0_bkpwr'], \
				['gpio4d6', 'sdio_intn'], \
				[''])

				# 2'b00
	GRF_GPIO5B_IOMUX	= (0x0050, \
				['gpio5b0', 'uart1bb_sin', 'ts0_data0', 'reserved'], \
				['gpio5b1', 'uart1bb_sout', 'ts0_data1', 'reserved'], \
				['gpio5b2', 'uart1bb_ctsn', 'ts0_data2', 'reserved'], \
				['gpio5b3', 'uart1bb_rtsn', 'ts0_data3', 'reserved'], \
				['gpio5b4', 'spi0_clk', 'ts0_data4', 'uart4exp_ctsn'], \
				['gpio5b5', 'spi0_csn0', 'ts0_data5', 'uart4exp_rtsn'], \
				['gpio5b6', 'spi0_txd', 'ts0_data6', 'uart4exp_sout'], \
				['gpio5b7', 'spi0_rxd', 'ts0_data7', 'uart4exp_sin'])

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

