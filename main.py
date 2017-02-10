from display import *
from draw import *

screen = new_screen()
color = [ 255, 0, 0 ]

draw_line( screen, 15, 15, 150, 150, color )

display(screen)
save_extension(screen, 'img.png')
