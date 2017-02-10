from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
	a = abs(y0 - y1)
	b = -(abs(x0 - x1))
	x = x0
	y = y0
	d = (2 * a) + b
	while (x <= x1):
		plot(screen, color, x, y)
		if (d > 0):
			y += 1
			d += (2 * b)
		x += 1
		d += (2 * a)
