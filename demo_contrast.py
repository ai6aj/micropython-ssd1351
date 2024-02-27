"""SSD1351 demo (contrast)."""
from time import sleep
from ssd1351 import color565, Display
from machine import Pin, SPI
from xglcd_font import XglcdFont
from demo_const import demo_const

def test():
    """Test code."""
    spi = demo_const.get_spi()
    display = demo_const.get_display(spi)
    display.contrast(0)
    display.draw_image('images/MicroPython128x128.raw',
                       0, 0, 128, 128)

    fixed_font = XglcdFont('fonts/FixedFont5x8.c', 5, 8)
    contrast_range = list(range(1, 16)) + list(reversed(range(15)))
    for c in contrast_range:
        display.contrast(c)
        display.draw_text(30, 120, 'contrast: {0:02d}'.format(c),
                          fixed_font, color565(255, 255, 255))
        sleep(1)

    display.cleanup()


test()
