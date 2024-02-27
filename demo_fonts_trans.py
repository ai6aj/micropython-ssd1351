"""SSD1351 demo (fonts-transparent)."""
from time import sleep
from ssd1351 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from demo_const import demo_const

def test():
    """Test code."""
    spi = demo_const.get_spi()
    display = demo_const.get_display(spi)

    display.draw_image('images/Tabby128x128.raw', 0, 0, 128, 128)

    print("Loading fonts, please wait.")
    fixed_font = XglcdFont('fonts/FixedFont5x8.c', 5, 8)
    unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24)
    print("Fonts loaded.")

    display.draw_text(0, 0, 'Not transparent', fixed_font,
                      color565(255, 0, 255))
    display.draw_text(0, 80, 'Transparent', unispace, color565(0, 128, 255),
                      spacing=0, transparent=True)
    display.draw_text(0, 103, 'Background', unispace, color565(0, 128, 255),
                      color565(255, 255, 255), spacing=0)
    display.draw_text(103, 20, 'Test', unispace, color565(0, 255, 128),
                      landscape=True, spacing=2, transparent=True)
    display.draw_text(0, 20, 'Test', unispace, color565(128, 255, 0),
                      landscape=True)





    sleep(9)
    display.cleanup()


test()
