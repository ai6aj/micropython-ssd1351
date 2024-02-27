from machine import Pin,SPI
from ssd1351 import Display, color565

class demo_const:
    def get_spi():
        return SPI(0,20_000_000)
    
    def get_display(spi=None):
        if not spi:
            return Display(demo_const.get_spi(), dc=demo_const.DC_PIN, cs=demo_const.CS_PIN, rst=demo_const.RST_PIN)    
        return Display(spi, dc=demo_const.DC_PIN, cs=demo_const.CS_PIN, rst=demo_const.RST_PIN)

    DC_PIN=Pin(2)
    RST_PIN=Pin(3)
    CS_PIN=Pin(22)
