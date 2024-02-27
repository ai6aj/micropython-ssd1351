"""SSD1351 demo (images)."""
from time import sleep
from ssd1351 import Display
from machine import Pin, SPI
from demo_const import demo_const

def test():
    """Test code."""
    spi = demo_const.get_spi()
    display = demo_const.get_display(spi)

    display.draw_image('images/RaspberryPiWB128x128.raw', 0, 0, 128, 128)
    sleep(5)

    display.draw_image('images/MicroPython128x128.raw', 0, 0, 128, 128)
    sleep(5)

    display.draw_image('images/Tabby128x128.raw', 0, 0, 128, 128)
    sleep(5)

    display.draw_image('images/Tortie128x128.raw', 0, 0, 128, 128)
    sleep(9)

    display.cleanup()


test()
