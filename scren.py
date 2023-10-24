import board
import displayio
from adafruit_st7789 import ST7789
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.polygon import Polygon

displayio.release_displays()

# Establish SPI interface
spi = board.SPI()
tft_cs = board.D5  # this is the CS pin you chose on the board
tft_dc = board.D6 # this is the DC pin you chose on the board
disp_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(disp_bus, rotation=270, width=240, height=135, rowstart=40,    colstart=53)  # this line and the one above is just a single line of code

my_group = displayio.Group()
display.show(my_group)  # clear the screen
my_bitmap = displayio.Bitmap(240, 135, 1) # width and height are your choice
my_palette = displayio.Palette(1) # number of palette colors
my_palette[0] = 0xFFFFFF # assign colors to palette list
my_tile_grid = displayio.TileGrid(my_bitmap, x=0, y=0, pixel_shader=my_palette)
my_group.append(my_tile_grid)  # updates the display with the new objects

#color outside of while true


while True:
    pass
