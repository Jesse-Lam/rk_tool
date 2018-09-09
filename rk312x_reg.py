
class RK312xRegMux:
	GRF_GPIO0A_IOMUX	= (0x00a8, \
				['gpio0a0', 'i2c0_scl'], \
				['gpio0a1', 'i2c0_sda'], \
				['gpio0a2', 'i2c1_scl'], \
				['gpio0a3', 'i2c1_sda', 'mmc1_cmd'], \
				[''], \
				[''], \
				['gpio0a6', 'i2c3_scl', 'hdmi_ddcscl'], \
				['gpio0a7', 'i2c3_sda', 'hdmi_ddcsda'])

	GRF_GPIO0B_IOMUX	= (0x00ac, \
				['gpio0b0', 'i2s_mclk'], \
				['gpio0b1', 'i2s_sclk', 'spi_clk'], \
				[''], \
				['gpio0b3', 'i2s_lrckrx', 'spi_txd'], \
				['gpio0b4', 'i2s_lrcktx'], \
				['gpio0b5', 'i2s_sdo', 'spi_rxd'], \
				['gpio0b6', 'i2s_sdi', 'spi_csn0'], \
				['gpio0b7', 'hdmi_hotplugin'])

	GRF_GPIO0C_IOMUX	= (0x00b0, \
				[''], \
				['gpio0c1', 'sc_io', 'uart0_rstn'], \
				[''], \
				[''], \
				['gpio0c4', 'hdmi_cecsda'], \
				[''], \
				[''], \
				['gpio0c7', 'nand_cs1'])

	GRF_GPIO0D_IOMUX	= (0x00b4, \
				['gpio0d0', 'uart2_rtsn'], \
				['gpio0d1', 'uart2_ctsn'], \
				['gpio0d2', 'pwm_0'], \
				['gpio0d3', 'pwm_1'], \
				['gpio0d4', 'pwm_2'], \
				[''], \
				['gpio0d6', 'mmc1_pwren'], \
				[''])

	GRF_GPIO1A_IOMUX	= (0x00b8, \
				['gpio1a0', 'i2s_mclk', 'sdmmc_clkout', 'xin32k'], \
				['gpio1a1', 'i2s_sclk', 'sdmmc_data0', 'pmic_sleep'], \
				['gpio1a2', 'i2s_lrckrx', 'sdmmc_data1'], \
				['gpio1a3', 'i2s_lrcktx'], \
				['gpio1a4', 'i2s_sdo', 'sdmmc_data2'], \
				['gpio1a5', 'i2s_sdi', 'sdmmc_data3'], \
				[''], \
				['gpio1a7', 'mmc0_wrprt'])

	GRF_GPIO1B_IOMUX	= (0x00bc, \
				['gpio1b0', 'spi_clk', 'uart1_ctsn'], \
				['gpio1b1', 'spi_txd', 'uart1_sout'], \
				['gpio1b2', 'spi_rxd', 'uart1_sin'], \
				['gpio1b3', 'spi_csn0', 'uart1_rtsn'], \
				['gpio1b4', 'spi_csn1'], \
				[''], \
				['gpio1b6', 'mmc0_pwren'], \
				['gpio1b7', 'mmc0_cmd'])

	GRF_GPIO1C_IOMUX	= (0x00c0, \
				['gpio1c0', 'mmc0_clkout'], \
				['gpio1c1', 'mmc0_detn'], \
				['gpio1c2', 'mmc0_d0', 'uart2_tx'], \
				['gpio1c3', 'mmc0_d1', 'uart2_rx'], \
				['gpio1c4', 'mmc0_d2', 'jtag_tck'], \
				['gpio1c5', 'mmc0_d3', 'jtag_tms'], \
				['gpio1c6', 'emmc_cmd', 'nand_cs2'], \
				['gpio1c7', 'emmc_rstnout', 'nand_cs3'])

	GRF_GPIO1D_IOMUX	= (0x00c4, \
				['gpio1d0', 'nand_d0', 'emmc_d0', 'sfc_d0'], \
				['gpio1d1', 'nand_d1', 'emmc_d1', 'sfc_d1'], \
				['gpio1d2', 'nand_d2', 'emmc_d2', 'scf_d2'], \
				['gpio1d3', 'nand_d3', 'emmc_d3', 'scf_d3'], \
				['gpio1d4', 'nand_d4', 'emmc_d4', 'spi_rxd1'], \
				['gpio1d5', 'nand_d5', 'emmc_d5', 'spi_txd1'], \
				['gpio1d6', 'nand_d6', 'emmc_d6', 'spi_csn0'], \
				['gpio1d7', 'nand_d7', 'emmc_d7', 'spi_csn1'])

	GRF_GPIO2A_IOMUX	= (0x00c8, \
				['gpio2a0', 'nand_ale', 'spk_clk'], \
				['gpio2a1', 'nand_cle'], \
				['gpio2a2', 'nand_wrn', 'sfc_csn0'], \
				['gpio2a3', 'nand_rdn', 'sfc_csn1'], \
				['gpio2a4', 'nand_rdy', 'emmc_cmd', 'sfc_clk'], \
				['gpio2a5', 'nand_wp', 'emmc_pwren'], \
				['gpio2a6', 'nand_cs0'], \
				['gpio2a7', 'nand_dqs', 'emmc_clkout'])

	GRF_GPIO2B_IOMUX	= (0x00cc, \
				['gpio2b0', 'lcdc0_dclk', 'ebc_sdclk', 'gmac_rxdv'], \
				['gpio2b1', 'lcdc0_hsync', 'ebc_sdle', 'gmac_txclk'], \
				['gpio2b2', 'lcdc0_vsync', 'ebc_sdoe', 'gmac_crs'], \
				['gpio2b3', 'lcdc0_den', 'ebc_gdclk', 'gmac_rxclk'], \
				['gpio2b4', 'lcdc0_d10', 'ebc_sdce2', 'gmac_mdio'], \
				['gpio2b5', 'lcdc0_d11', 'ebc_sdce3', 'gmac_txen'], \
				['gpio2b6', 'lcdc0_d12', 'ebc_sdce4', 'gmac_clk'], \
				['gpio2b7', 'lcdc0_d13', 'ebc_sdce5', 'gmac_rxer'])

	GRF_GPIO2C_IOMUX	= (0x00d0, \
				['gpio2c0', 'lcdc0_d14', 'ebc_vcom', 'gmac_rxd1'], \
				['gpio2c1', 'lcdc0_d15', 'ebc_gdoe', 'gmac_rxd0'], \
				['gpio2c2', 'lcdc0_d16', 'ebc_gdsp', 'gmac_txd1'], \
				['gpio2c3', 'lcdc0_d17', 'ebc_gdpwr0', 'gmac_txd0'], \
				[''], \
				[''], \
				[''], \
				[''])

	GRF_GPIO2D_IOMUX	= (0x00d4, \
				[''], \
				['gpio2d1', 'lcdc0_d23', 'ebcc_gdpwr2', 'gmac_mdc'], \
				['gpio2d2', 'sc_rst', 'uart0_sout'], \
				['gpio2d3', 'sc_clk', 'uart0_sin'], \
				[''], \
				['gpio2d5', 'sc_det', 'uart0_ctsn'], \
				['gpio2d0', 'lcdc0_d22', 'ebc_gdpwr1', 'gsp_clk', 'gmac_col'], \
				[''])

	GRF_GPIO3B_IOMUX	= (0x00dc, \
				[''], \
				[''], \
				[''], \
				['gpio3a3', 'testclk_out'], \
				[''], \
				[''], \
				[''], \
				[''])

	GRF_GPIO3C_IOMUX	= (0x00e0, \
				[''], \
				['gpio3c1', 'otg_drvvbus'], \
				[''], \
				[''], \
				[''], \
				[''], \
				[''], \
				[''])

	GRF_GPIO3D_IOMUX	= (0x00e4, \
				[''], \
				[''], \
				['gpio3d2', 'pwm_irin'], \
				['gpio3d3', 'spdif_tx'], \
				[''], \
				[''], \
				[''], \
				[''])

	GRF_GPIO2C_IOMUX	= (0x00e8, \
				['gpio2c4', 'lcdc0_d18', 'ebc_gdrl', 'i2c2_sda', 'gmac_rxd3'], \
				['gpio2c5', 'lcdc0_d19', 'ebc_sdshr', 'i2c2_scl', 'gmac_rxd2'], \
				['gpio2c6', 'lcdc0_d20', 'ebc_border0', 'gps_sign', 'gmac_txd2'], \
				['gpio2c7', 'lcdc0_d21', 'ebc_border1', 'gps_mag', 'gmac_txd3'])


