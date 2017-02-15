from display import *

def draw_line1( screen, x0, y0, x1, y1, color ):
	a = y1 - y0
	b = x0 - x1
	x = x0
	y = y0
	d = (2 * a) + b
	while (x < x1):
		plot(screen, color, x, y)
		if (d > 0):
			y += 1
			d += (2 * b)
		x += 1
		d += (2 * a)

def draw_line8( screen, x0, y0, x1, y1, color ):
	a = y1 - y0
	b = x0 - x1
	x = x0
	y = y0
	d = (2 * a) - b
	while (x < x1):
		plot(screen, color, x, y)
		if (d < 0):
			y -= 1
			d -= (2 * b)
		x += 1
		d += (2 * a)

def draw_line2( screen, x0, y0, x1, y1, color ):
	a = y1 - y0
	b = x0 - x1
	x = x0
	y = y0
	d = a + (2 * b)
	while (y < y1):
		plot(screen, color, x, y)
		if (d < 0):
			x += 1
			d += (2 * a)
		y += 1
		d += (2 * b)

def draw_line7( screen, x0, y0, x1, y1, color ):
	a = y1 - y0
	b = x0 - x1
	x = x0
	y = y0
	d = a - (2 * b)
	while (y > y1):
		plot(screen, color, x, y)
		if (d > 0):
			x += 1
			d += (2 * a)
		y -= 1
		d -= (2 * b)

def draw_line(screen, x0, y0, x1, y1, color):
	dx = x1 - x0
	dy = y1 - y0
	if (dy >= 0):
		if (dy > dx):
			draw_line2(screen, x0, y0, x1, y1, color)
		else:
			draw_line1(screen, x0, y0, x1, y1, color)
	else:
		if (-dy > dx):
			draw_line7(screen, x0, y0, x1, y1, color)
		else:
			draw_line8(screen, x0, y0, x1, y1, color)




# def draw_line(screen, x0, y0, x1, y1, color):
#     dx = abs(x1 - x0)
#     dy = abs(y1 - y0)
#     x = x0
#     y = y0
#     sx = -1 if x0 > x1 else 1
#     sy = -1 if y0 > y1 else 1
#     if dx > dy:
#         diff = dx / 2.0
#         while x != x1:
#             plot(screen, color, x, y)
#             diff -= dy
#             if diff < 0:
#                 y += sy
#                 diff += dx
#             x += sx
#     else:
#         diff = dy / 2.0
#         while y != y1:
#             plot(screen, color, x, y)
#             diff -= dx
#             if diff < 0:
#                 x += sx
#                 diff += dy
#             y += sy        
#     plot(screen, color, x, y)






