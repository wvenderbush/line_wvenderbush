#!/usr/bin/python

from display import *
from draw import *
import os

screen = new_screen()
color1 = [ 255, 0, 0 ]
color2 = [ 0, 255, 0 ]
color7 = [ 0, 255, 255 ]
color8 = [255, 0 , 255]
colorst = [100, 255, 0]
colorvt = [255, 255, 0]
color15 = [255, 100, 0]
color25 = [0, 100, 255]

draw_line( screen, 150, 150, 400, 350, color1 )
draw_line( screen, 200, 100, 300, 400, color2 )
draw_line( screen, 200, 400, 350, 100, color7 ) 
draw_line( screen, 150, 350, 400, 150, color8 )

draw_line( screen, 50, 50, 400, 50, colorst)
draw_line( screen, 400, 400, 400, 50, colorvt)

draw_line( screen, 50, 150, 450, 350, color15 )
draw_line( screen, 50, 350, 450, 200, color25 )




display(screen)
save_extension(screen, 'img.png')

