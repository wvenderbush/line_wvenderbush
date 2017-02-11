from display import *
from draw import *

screen = new_screen()
color = [ 255, 0, 0 ]

draw_line( screen, 0, 0, 500, 500, color )

display(screen)
save_extension(screen, 'img.png')
