"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import random
import pygame

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
purple = (113, 33, 148)
orange = (235, 157, 23)
pink = (237, 130, 200)

colors = [blue, red, purple, white, black, orange, pink]
ball_color = random.choice(colors)

x = 30
y = 30
dx = 3
dy = 3 

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:

	for event in pygame.event.get():
	
		if event.type == pygame.QUIT:
			done = True
			
		elif event.type == pygame.MOUSEBUTTONDOWN :
			location = pygame.mouse.get_pos()
			x,y = location

	screen.fill(green)

	pygame.draw.circle(screen, ball_color, (x, y), 30, 0)
	
	x = x + dx
	y = y + dy
		
	if x>670:
		dx = dx*-1
	if x<30:
		dx = dx*-1
	if y>470:
		dy = dy*-1
	if y<30:
		dy = dy*-1
		
	pygame.display.flip()

	clock.tick(60)

pygame.quit()
exit()
