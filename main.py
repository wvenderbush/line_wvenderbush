#!/usr/bin/python

from display import *
from draw import *
import os

screen = new_screen()
color1 = [ 255, 0, 0 ]
color2 = [ 0, 255, 0 ]
color7 = [ 0, 255, 255 ]
color8 = [255, 0 , 255]

draw_line1( screen, 150, 150, 350, 350, color1 )
draw_line2( screen, 200, 100, 300, 400, color2 )
draw_line7( screen, 150, 350, 350, 150, color7 ) #?? why is this 8 and why is the other 7?
draw_line8( screen, 200, 400, 300, 100, color8 ) #???

# draw_line( screen, 150, 150, 350, 350, color1 )
# draw_line( screen, 200, 100, 300, 400, color2 )
# draw_line( screen, 150, 350, 350, 150, color7 )
# draw_line( screen, 200, 400, 300, 100, color8 )




display(screen)
save_extension(screen, 'img.png')

